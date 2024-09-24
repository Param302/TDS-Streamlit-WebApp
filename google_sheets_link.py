import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope (permissions)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

cloud_creds = json.load(open("sheets_api_creds.json"))
creds = ServiceAccountCredentials.from_json_keyfile_dict(cloud_creds, scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open('TDS Streamlit Web App').sheet1
sheet.clear()
print(sheet.get_all_records())
sheet.update_acell("A1", "=SUM(ARRAY_CONSTRAIN(SEQUENCE(100, 100, 2, 6), 1, 10))")
print(sheet.get_values("A1"))