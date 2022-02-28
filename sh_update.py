import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='novice.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['Marry','Tim','Carl']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('SH1')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))