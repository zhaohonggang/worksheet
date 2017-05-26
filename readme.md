##Installation and run(Tested in python3):
0. save client_secret.json into working directory by following the introduction: https://developers.google.com/sheets/api/quickstart/python
   enable google api for the following scopes:
	  'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/spreadsheets'
1. virtualenv worksheet
2. worksheet\Scripts\activate.bat
3. pip install -r requirements.txt
4. python json2csv.py rights.json output.csv
5. verify output.csv in created in google drive
