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
ad =  [["1/1/2020", 4000, 'hello'],["5/2/2021", 4900, 'Namste'],["8/3/2020", 5000, 'hi'],["12/12/2012", 1000, 'halo'],["15/01/2023", 9020, "kon'nichiwa"]]

for i in ad:
    z += 1
    celup = 'A'+str(z)+':'+'C'+str(z)
    sheet.update(celup,[i])
