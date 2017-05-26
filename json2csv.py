'''
python json2csv.py rights.json output.csv
'''

import utils as ut
import pandas as pd
import sys
from quickstart import get_credentials
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

#print(sys.argv)


jsonfile = sys.argv[1]
csvfile = sys.argv[2]


#json to csv

j = ut.readFile(jsonfile)
df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in j.items()]))  
df = df.stack().to_frame(name='r')
df.index = df.index.droplevel()
df.reset_index(inplace=True)
df['v'] = 1
df=df.groupby(['index','r'])['v'].mean()
df=df.unstack().fillna(0)
df.sort_index(axis=1,ascending=False)
df = df.reindex_axis(['view_grades', 'change_grades', 'add_grades', 'delete_grades', 'view_classes', 'change_classes', 'add_classes', 'delete_classes'], axis=1)
df = df.reindex_axis(['student1', 'student2', 'teacher', 'principle'], axis=0)
df.to_csv(csvfile)


#to google drive
df.reset_index(inplace=True)
credentials = get_credentials()
gc = gspread.authorize(credentials)
sh = gc.create(csvfile)
#worksheet = sh.add_worksheet(title="A worksheet", rows="5", cols="9")
worksheet = sh.get_worksheet(0)
set_with_dataframe(worksheet, df)

