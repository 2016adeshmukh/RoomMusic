import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https//spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("TestSheet").sheet0

wks.update_acell('A1', "Test this")

