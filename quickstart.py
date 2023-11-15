from googleapiclient.discovery import build
from google.oauth2 import service_account
from wrangle import DataProcessor

file_path = "data.txt"  # Adjust the file path as needed
processor = DataProcessor(file_path)
df = processor.main()
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
SAMPLE_SPREADSHEET_ID = '10NQm6QiCMsHq2EWpt93_dCFQEuWxf7RUq_FZw2ZCT_U'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
# In order to read the values from spreadsheet use the below commented code

# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="sales!a1:b6").execute()
# values = result.get('values', [])

#переменная с ручным массивом работает
aoa = [["lastChangeDate", "2023-10-19T03,50,53"],["1/1/2222",5000],["1/1/2222",7000]]

#переменная с values_to_write (файл file_path = "data_copy.txt") - работает

#!!!не работает, если изменить в строке 5 data_copy.txt на data221.json


request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="PnL!B2", valueInputOption="USER_ENTERED", body=dict(majorDimension='ROWS',
                                                                                          values=values_to_write)).execute()
# print(values)
print(request)
