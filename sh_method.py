# import pygsheets
# import pandas as pd
# from google.oauth2 import service_account
# from googleapiclient.discovery import build

# from sh_read import SCOPES

# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# creds = service_account.Credentials.from_service_account_file("novice.json", scopes= SCOPES)
# # SAMPLE_SPREADSHEET_ID = '1Ax-Q0bXlCe5jyB72WIqi446y0yL6NNHmv9iPJq_kjxg'
# service = build('sheets', 'v4', credentials=creds)
# sheet = creds.open("SH1").get_worksheet(1)
# a = len(sheet.col_values(1))
# ad =  [["1/1/2020",4000],["5/2/2021",4900],["8/3/2020", 5000]]
# # for i in sheet:
# # r = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
# #                                            range="Sheet2!B2", valueInputOption="USER_ENTERED", 
# #                                            body={"values":ad})
    
#     # r = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#     #                                                  range="Sheet2!B2", valueInputOption="USER_ENTERED", 
#     #                                                  insertDataOption="INSERT_ROWS", body={"values":ad})
#     # response = r.execute()

# # print(response)

# print(a)


#  Library for google-Sheet

from oauth2client.service_account import ServiceAccountCredentials
import json
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("novice.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("SH1").get_worksheet(1)  #open sheet
# print(sheet)
z=len(sheet.col_values(1))
print(z)