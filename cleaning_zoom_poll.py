# ###############################################
# The purpose of this script is to automate the retrieval, consolidation, and update process cleaning zoom pole files
# 1. Read spreadsheets from google drive, pulling a data frame for each question
# 2. Consolidate data frames for all
# created by: E Miller
# last updated: 10/14/24
# ###############################################
import os.path
import os 
os.environ['APPDATA'] = ""
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from pandasgui import show
import numpy as np

import plotly
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.offline import init_notebook_mode
import plotly.io as pio

pio.renderers.default = "browser"

pd.options.mode.chained_assignment = None  # default='warn'

# print(pio.renderers)


# init_notebook_mode(connected = True) 



# # authorization for google
# gc = gspread.oauth()

# # identify question numbers and set as variables
# q1 = 'Question 1: CHW Autonomy'
# q2 = 'Question 2: CHW Workforce Retention and Burnout'
# q3 = 'Question 3: CHW Role and Institutional Support'
# q4 = 'Question 4: CHW Supervision'
# q5 = 'Question 5: MCOs and Care Coordination'

# # print(q1)



# # import questions: is there a way to find based on wildcard logic?

# def wrapper(sht):
#     zp_import_file = gc.open_by_key('1qA5FQRmTilFFdZ-nEw9DJ-9_GMcnHw_NZVoM6K3P8H8')
#     zp_worksheet_import = zp_import_file.worksheet(sht)
#     zp_q1 = zp_worksheet_import.find(q1, in_column=1)
#     zp_q2 = zp_worksheet_import.find(q2, in_column=1)
#     zp_q3 = zp_worksheet_import.find(q3, in_column=1)
#     zp_q4 = zp_worksheet_import.find(q4, in_column=1)
#     zp_q5 = zp_worksheet_import.find(q5, in_column=1)


#     # get starting point of rows
#     zp_row_start_r1 = zp_q1.row
#     zp_row_start_r2 = zp_q2.row
#     zp_row_start_r3 = zp_q3.row
#     zp_row_start_r4 = zp_q4.row
#     zp_row_start_r5 = zp_q5.row
#     zp_row_start_last = zp_row_start_r4 + zp_row_start_r5



#     # Get Responses as Data Frames
#     def get_responses(zp_start_res, zp_start_next_res):
#         zp_res_df_raw = get_as_dataframe(zp_worksheet_import,usecols = [0,1,2,3,4],skiprows = zp_start_res, nrows = zp_start_next_res - zp_start_res - 2)
#         zp_res_df = zp_res_df_raw.dropna(subset = ['User Name'], how = 'any')
#         return zp_res_df

#     zp_r1_df = get_responses(zp_row_start_r1, zp_row_start_r2)
#     zp_r2_df = get_responses(zp_row_start_r2, zp_row_start_r3)
#     zp_r3_df = get_responses(zp_row_start_r3, zp_row_start_r4)
#     zp_r4_df = get_responses(zp_row_start_r4, zp_row_start_r5)
#     zp_r5_df = get_responses(zp_row_start_r5, zp_row_start_last)

#     # print(zp_r1_df)

#     # Get Questions as data frames
#     def get_questions(zp_start_res):
#         zp_q_raw = get_as_dataframe(zp_worksheet_import,usecols = [4], skiprows = zp_start_res, nrows = 1)
#         zp_q = zp_q_raw.columns[0]
#         return zp_q

#     zp_q1 = get_questions(zp_row_start_r1)
#     zp_q2 = get_questions(zp_row_start_r2)
#     zp_q3 = get_questions(zp_row_start_r3)
#     zp_q4 = get_questions(zp_row_start_r4)
#     zp_q5 = get_questions(zp_row_start_r5)

#     # # Clean Questions Data Frames: re-order columns, remove unneeded characters, re-set data types
#     def qframe_clean(zp_df, zp_q, q_cat):
#         zp_q_df = zp_df
#         zp_q_df.columns = ['RESPONSE_ID','USER_NAME','EMAIL_ADDRESS','SUBMITTED_DATE','RESPONSE']
#         zp_q_df['QUESTION'] = zp_q
#         zp_q_df['QUESTION_CATEGORY'] = q_cat

#         # df = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
#         conditions = [
#             (zp_q_df['QUESTION_CATEGORY'] == q1),
#             (zp_q_df['QUESTION_CATEGORY'] == q2),
#             (zp_q_df['QUESTION_CATEGORY'] == q3),
#             (zp_q_df['QUESTION_CATEGORY'] == q4),
#             (zp_q_df['QUESTION_CATEGORY'] == q5)
#             ]
#         choices = [1,2,3,4,5]
#         zp_q_df['QUESTION_NUMBER'] = np.select(conditions, choices)
#                                         #   , default='black')
#         # print(zp_q_df)


#         return zp_q_df

#     zp_q1_clean = qframe_clean(zp_r1_df, zp_q1, q1)
#     zp_q2_clean = qframe_clean(zp_r2_df, zp_q2, q2)
#     zp_q3_clean = qframe_clean(zp_r3_df, zp_q3, q3)
#     zp_q4_clean = qframe_clean(zp_r4_df, zp_q4, q4)
#     zp_q5_clean = qframe_clean(zp_r5_df, zp_q5, q5)

#     # Concatenate Responses dataframe
#     zp_qs_raw = pd.concat([zp_q1_clean,zp_q2_clean,zp_q3_clean,zp_q4_clean,zp_q5_clean], axis=0).reset_index(drop=True)

#     return zp_qs_raw


# wksheet1 = wrapper('Sheet1')
# wksheet2 = wrapper('Sheet2')
# wksheet3 = wrapper('Sheet3')

# # print(wksheet1)

# # Concatenate Responses from consolidated worksheets
# zp_data_set = pd.concat([wksheet1,wksheet2,wksheet3], axis=0).reset_index(drop=True)

# # print(zp_data_set)

# show(zp_data_set)




# # create graph for question 1 using plotly

# # countries on x-axis
# responses=['Strongly Agree', 'Agree',
#            'Neutral','Disagree',
#            'Strongly Disagree'] 


# pivot and filter dataframe:
# filter by question number 


# pivot to show responses and counts




# create array of response_num, response_text, and count of responses 

# add numbers to responses ('1-Strongly Disagree','2-Disagree'...)
# pivot to show responses and counts
# create array of responses and count 
# plot the array?
# or create 2 lists to plot?

# # plotting corresponding y for each 
# # country in x 
# fig = go.Figure([go.Bar(x=responses,
#                         y=[4,10,2,1,1])]) 

# fig.show() 