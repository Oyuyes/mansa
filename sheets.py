import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from config import SHEET_ID

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load JSON credentials from environment
creds_dict = json.loads(os.environ["GOOGLE_CREDS_JSON"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(SHEET_ID).worksheet("Subscribers")

def log_subscription(name, user_id, duration):
    sheet.append_row([name, str(user_id), duration])
