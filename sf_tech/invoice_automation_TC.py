# ###############################################
# The purpose of this script is to automate the retrieval, consolidation, and update process for monthly invoices.
# 1. Read spreadsheets from google drive, pulling in only relevant data
# 2. Consolidate invoices for all
# 3. Breakdown of hours and dollars by client for current month (deduped so that clients are not double charged for meeting attendance)
# 4. Breakdown of hours and dollars by contractor
# 5. Tracking of remaining hours by client
# created by: E Miller
# last updated: 6/01/24

# ###############################################


import os.path
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

# authorization for google
gc = gspread.oauth()

# date/name of tab in spreadsheet to extract data
wkst = 'Nov_5'


#########################
# function to get invoices
#########################
def invoice_import(ik):
    invoice_import_file = gc.open_by_key(ik)
    invoice_worksheet_import = invoice_import_file.worksheet(wkst)
    invoice_df_raw = get_as_dataframe(invoice_worksheet_import,usecols = [0,1,2,3,4,5,6,7,8],skiprows = 12)
    invoice_name_raw = get_as_dataframe(invoice_worksheet_import,usecols = [0],nrows = 1)
    invoice_name = invoice_name_raw.columns[0]

    
    # restructure columns and remove empty rows in first frame
    invoice_columns = invoice_df_raw[['SERVICE DESCRIPTION','SERVICE DATE','MEETING?','MEETING TIME','CLIENT/GRANT','CATEGORY','TOTAL HOURS','RATE']]

    #  pull in only rows that have record of work
    invoice = invoice_columns.dropna(subset = ['SERVICE DESCRIPTION'], how = 'any')

    # add columns for Total and Contractor Name
    invoice['TOTAL HOURS'] = invoice['TOTAL HOURS'].astype('float')
    invoice['TOTAL DOLLARS'] = invoice['TOTAL HOURS'] * invoice['RATE']
    invoice['CONTRACTOR NAME'] = invoice_name

    return invoice 




#########################
# import invoices, consolidate to one sheet 
#########################

# get individual invoices
# person_1 
invoice_1 = invoice_import('sheet_id_person_1')
# person_2
invoice_2 = invoice_import('sheet_id_person_2') 
# person_3
invoice_3 = invoice_import('sheet_id_person_3')

# consolidate to one sheet
invoice_totals = pd.concat([invoice_1, invoice_2,invoice_3
                            ], axis=0).reset_index(drop=True)      # axis = 0 for concatenating rows

# re-order columns, remove unneeded characters, re-set data types
invoice_totals = invoice_totals[['CONTRACTOR NAME','SERVICE DESCRIPTION','SERVICE DATE','MEETING?','MEETING TIME','CLIENT/GRANT','CATEGORY', 'TOTAL HOURS','RATE','TOTAL DOLLARS']]
invoice_totals['SERVICE DATE'] = invoice_totals['SERVICE DATE'].astype('datetime64[ns]')
invoice_totals['ORGANIZATION'] = 'Transformative Changes'



#########################
# perform aggregations and write to google sheet tabs
#########################
# google sheet location
sh = gc.open_by_key('output_sheet')

# get total hours for TC and write to second tab. the first tab is created last 
tc_invoice_totals = invoice_totals.groupby('ORGANIZATION').agg({'TOTAL HOURS':'sum','TOTAL DOLLARS':'sum'}).reset_index()
worksheet = sh.get_worksheet(1)
set_with_dataframe(worksheet, tc_invoice_totals)

##### group hours and dollars by contractor and write to third tab 
group_by_name = invoice_totals.groupby(['CONTRACTOR NAME']).agg({'TOTAL HOURS':'sum','TOTAL DOLLARS':'sum'}).reset_index()
group_by_name.loc[''] = group_by_name.sum(numeric_only=True)
group_by_name[['CONTRACTOR NAME']] = group_by_name[['CONTRACTOR NAME']].fillna(value='Totals')
worksheet = sh.get_worksheet(2)
set_with_dataframe(worksheet, group_by_name)


# Dedupe hours, group by client, and write to fourth tab 
    # create data frame that has only entries without meetings, or the client is TC
no_meetings_df = invoice_totals.loc[(invoice_totals['MEETING?'] == 0)|(invoice_totals['MEETING TIME'].isnull()) | (invoice_totals['CLIENT/GRANT'] == 'TC')]

# create data frame with meetings where client is not TC and dedupe. 
    # When multiple people are in the same meeting, 
    # take the amount and hours from the contractor that billed the most
meetings_df = invoice_totals.loc[(invoice_totals['MEETING?'] == 1)|((invoice_totals['MEETING TIME'].notnull()) & (invoice_totals['CLIENT/GRANT'] != 'TC'))]
meetings_df_deduped = meetings_df.sort_values('TOTAL HOURS', ascending=False).drop_duplicates(['SERVICE DATE', 'MEETING TIME','CLIENT/GRANT']).sort_index() 

# concatenate frames for deduped data for clients
invoice_totals_deduped_raw = pd.concat([no_meetings_df,meetings_df_deduped]).sort_index()
invoice_totals_deduped = invoice_totals_deduped_raw[invoice_totals_deduped_raw['CLIENT/GRANT'] != 'TC']




# create aggregated totals for clients
tc_rate = <rate integer>
group_by_client = invoice_totals_deduped.groupby(['CLIENT/GRANT']).agg({'TOTAL HOURS':'sum'}).reset_index()
group_by_client['TC DOLLARS'] = group_by_client['TOTAL HOURS'] * tc_rate
group_by_client.loc[''] = group_by_client.sum(numeric_only=True, axis=0)
group_by_client[['CLIENT/GRANT']] = group_by_client[['CLIENT/GRANT']].fillna(value='Totals')

worksheet = sh.get_worksheet(3)
set_with_dataframe(worksheet, group_by_client)


# invoicetotals with all necessary data. write to first tab #########################
invoice_totals.loc[''] = invoice_totals[['TOTAL HOURS','TOTAL DOLLARS']].sum(numeric_only=True, axis=0)
invoice_totals[['CONTRACTOR NAME']] = invoice_totals[['CONTRACTOR NAME']].fillna(value='Totals')
worksheet = sh.get_worksheet(0)
set_with_dataframe(worksheet, invoice_totals)


#########################
# create itemized client invoices
#########################
# client invoice function
def client_invoice(client_name, wkst_num):
    client_invoice_raw = invoice_totals_deduped_raw[invoice_totals_deduped_raw['CLIENT/GRANT'] == client_name].reset_index(drop=True)
    client_invoice = client_invoice_raw[['SERVICE DESCRIPTION', 'SERVICE DATE','CATEGORY','TOTAL HOURS']]
    client_invoice['RATE'] = tc_rate
    client_invoice['TOTAL DOLLARS'] = client_invoice['TOTAL HOURS'] * client_invoice['RATE']

    client_invoice.loc[''] = client_invoice[['TOTAL HOURS','TOTAL DOLLARS']].sum(numeric_only=True, axis=0)
    client_invoice[['CATEGORY']] = client_invoice[['CATEGORY']].fillna(value='Totals')


    worksheet = sh.get_worksheet(wkst_num)
    set_with_dataframe(worksheet, client_invoice)

    return

# itemized client invoices
client_invoice('client_1', 4)
client_invoice('client_2', 5)


