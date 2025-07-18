# ###############################################
# The purpose of this script is to automate the retrieval, consolidation, and update process cleaning zoom pole files
# 1. Read spreadsheets from google drive, pulling a data frame for each question
# 2. Consolidate data frames for all
# created by: E Miller
# last updated: 10/14/24
# ###############################################
import os.path
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from pandasgui import show
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

# authorization for google
gc = gspread.oauth()

# identify question numbers and set as variables
q1 = 'Question 1: CHW Autonomy'
q2 = 'Question 2: CHW Workforce Retention and Burnout'
q3 = 'Question 3: CHW Role and Institutional Support'
q4 = 'Question 4: CHW Supervision'
q5 = 'Question 5: MCOs and Care Coordination'

print(q1)

# # import questions: is there a way to find based on wildcard logic?
# zp_import_file = gc.open_by_key('1qA5FQRmTilFFdZ-nEw9DJ-9_GMcnHw_NZVoM6K3P8H8')
# zp_worksheet_import = zp_import_file.worksheet('Sheet1')
# zp_q1 = zp_worksheet_import.find(q1, in_column=1)
# zp_q2 = zp_worksheet_import.find(q2, in_column=1)
# zp_q3 = zp_worksheet_import.find(q3, in_column=1)
# zp_q4 = zp_worksheet_import.find(q4, in_column=1)
# zp_q5 = zp_worksheet_import.find(q5, in_column=1)


# # get starting point of rows
# zp_row_start_r1 = zp_q1.row
# zp_row_start_r2 = zp_q2.row
# zp_row_start_r3 = zp_q3.row
# zp_row_start_r4 = zp_q4.row
# zp_row_start_r5 = zp_q5.row
# zp_row_start_last = zp_row_start_r4 + zp_row_start_r5



# # Get Responses as Data Frames
# def get_responses(zp_start_res, zp_start_next_res):
#     zp_res_df_raw = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_start_res, nrows = zp_start_next_res - zp_start_res - 2)
#     zp_res_df = zp_res_df_raw.dropna(subset = ['User Name'], how = 'any')
#     return zp_res_df

# zp_r1_df = get_responses(zp_row_start_r1, zp_row_start_r2)
# zp_r2_df = get_responses(zp_row_start_r2, zp_row_start_r3)
# zp_r3_df = get_responses(zp_row_start_r3, zp_row_start_r4)
# zp_r4_df = get_responses(zp_row_start_r4, zp_row_start_r5)
# zp_r5_df = get_responses(zp_row_start_r5, zp_row_start_last)

# print(zp_r1_df)

# # Get Questions as data frames
# def get_questions(zp_start_res):
#     zp_q_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_start_res, nrows = 1)
#     zp_q = zp_q_raw.columns[0]
#     return zp_q

# zp_q1 = get_questions(zp_row_start_r1)
# zp_q2 = get_questions(zp_row_start_r2)
# zp_q3 = get_questions(zp_row_start_r3)
# zp_q4 = get_questions(zp_row_start_r4)
# zp_q5 = get_questions(zp_row_start_r5)


# # # Clean Questions Data Frames: re-order columns, remove unneeded characters, re-set data types
# def qframe_clean(zp_df, zp_q, q_num):
#     zp_q_df = zp_df
#     zp_q_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
#     zp_q_df['QUESTION'] = zp_q
#     zp_q_df['QUESTION_NUMBER'] = q_num

#     return zp_q_df


# zp_q1_clean = qframe_clean(zp_r1_df, zp_q1, q1)
# zp_q2_clean = qframe_clean(zp_r2_df, zp_q2, q2)
# zp_q3_clean = qframe_clean(zp_r3_df, zp_q3, q3)
# zp_q4_clean = qframe_clean(zp_r4_df, zp_q4, q4)
# zp_q5_clean = qframe_clean(zp_r5_df, zp_q5, q5)

# # print(zp_q1_clean)

# # Concatenate Responses dataframe

# zp_qs_raw = pd.concat([zp_q1_clean,zp_q2_clean,zp_q3_clean,zp_q4_clean,zp_q5_clean], axis=0).reset_index(drop=True)


# show(zp_qs_raw)

# use pandas-gui to create bar graph(s)



# # Question 1
# zp_q1_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
# zp_q1_df['QUESTION'] = zp_q1
# zp_q1_df['QUESTION_NUMBER'] = q1



# # Question 2
# zp_q2_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
# zp_q2_df['QUESTION'] = zp_q2
# zp_q2_df['QUESTION_NUMBER'] = q2

# # Question 3
# zp_q3_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
# zp_q3_df['QUESTION'] = zp_q3
# zp_q3_df['QUESTION_NUMBER'] = q3

# # Question 4
# zp_q4_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
# zp_q4_df['QUESTION'] = zp_q4
# zp_q4_df['QUESTION_NUMBER'] = q4

# # Question 5
# zp_q5_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
# zp_q5_df['QUESTION'] = zp_q5
# zp_q5_df['QUESTION_NUMBER'] = q5



# # # Question 1
# # zp_q1_df = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_row_start_q1, nrows = zp_row_start_q2 - zp_row_start_q1 - 2)
# # zp_q1_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_row_start_q1, nrows = 1)
# # zp_q1 = zp_q1_raw.columns[0]


# # # Question 2
# # zp_q2_df = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_row_start_q2, nrows = zp_row_start_q3 - zp_row_start_q2 - 2)
# # zp_q2_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_row_start_q2, nrows = 1)
# # zp_q2 = zp_q2_raw.columns[0]

# # # Question 3
# # zp_q3_df = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_row_start_q3, nrows = zp_row_start_q4 - zp_row_start_q3 - 2)
# # zp_q3_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_row_start_q3, nrows = 1)
# # zp_q3 = zp_q3_raw.columns[0]

# # # Question 4
# # zp_q4_df = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_row_start_q4, nrows = zp_row_start_q5 - zp_row_start_q4 - 2)
# # zp_q4_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_row_start_q4, nrows = 1)
# # zp_q4 = zp_q4_raw.columns[0]

# # # # Question 5
# # # zp_q5_df = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_row_start_q5, nrows = zp_row_start_q6 - zp_row_start_q5 - 2)
# # # zp_q5_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_row_start_q5, nrows = 1)
# # # zp_q5 = zp_q5_raw.columns[0]







#     # #########################
#     # # restructure columns and remove empty rows in first frame
#     # #########################
#     # invoice_columns = invoice_df_raw[['SERVICE DESCRIPTION','SERVICE DATE','MEETING TIME','CLIENT/GRANT','CATEGORY','TOTAL HOURS','RATE']]
#     # #  pull in only rows that have record of work
#     # invoice = invoice_columns.dropna(subset = ['SERVICE DESCRIPTION'], how = 'any')
#     # # add columns for Total and Contractor Name
#     # invoice['TOTAL HOURS'] = invoice['TOTAL HOURS'].astype('float')
#     # invoice['TOTAL DOLLARS'] = invoice['TOTAL HOURS'] * invoice['RATE']
#     # invoice['CONTRACTOR NAME'] = invoice_name


#     # return zp_question 


# # get individual invoices
# # Ed 
# zp_wksht1_sht1_q1 = zp_import('1qA5FQRmTilFFdZ-nEw9DJ-9_GMcnHw_NZVoM6K3P8H8','Sheet1',)