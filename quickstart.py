from googleapiclient.discovery import build
from google.oauth2 import service_account
import wrangling

file_path = "data_copy.txt"
df = wrangling.main(file_path)
df.insert(0, 'Ticker', df.index)
values_to_write = df.T.reset_index().T.values.tolist()

SERVICE_ACCOUNT_FILE = 'keys.json'
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1dTfWTCVFOftX3_lePmXKkz9Zve8Kl0nVZ1jA7KjAMXo'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# In order to read the values from spreadsheet use the below commented code

# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="sales!a1:b6").execute()
# values = result.get('values', [])

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="PnL!B2", valueInputOption="USER_ENTERED", body=dict(majorDimension='ROWS',
                                                                                          values=values_to_write)).execute()
# print(values)
print(request)
