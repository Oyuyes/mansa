import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open sheets
subscriptions_sheet = client.open("tipsmansabot").worksheet("subscriptions")
odds_sheet = client.open("tipsmansabot").worksheet("daily_odds")

def fetch_latest_odds():
    records = odds_sheet.get_all_records()
    if records:
        latest = records[-1]
        return latest
    return None

def get_subscribers():
    records = subscriptions_sheet.get_all_records()
    active_users = [str(record['user_id']) for record in records if record['status'] == 'active']
    return active_users

def check_subscriptions(context):
    records = subscriptions_sheet.get_all_records()
    for i, record in enumerate(records):
        if record['status'] == 'active':
            start_date = datetime.strptime(record['start_date'], '%Y-%m-%d')
            duration = int(record['duration_days'])
            if datetime.now() > start_date + timedelta(days=duration):
                subscriptions_sheet.update_cell(i+2, 5, 'expired')  # Assuming 'status' is column 5
