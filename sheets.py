import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Sheet:
    ''' 
        Sheet manages all interactions with the Google Sheet
    '''

    def __init__(self, config):
        creds = ServiceAccountCredentials.from_json_keyfile_dict(config.getGoogleCredentials())
        client = gspread.authorize(creds)
        self.sheet = client.open_by_key(config.getSheetId()).sheet1

    def clear_sheet(self):
        self.sheet.clear()

    def upload_data(self, columns, data, date_time=False):
        sheet = self.sheet

        # Column names get inserted
        count = 1
        for column_name in columns:
            sheet.update_cell(1, count, column_name)
            count += 1

        # Current date added for diagnostic purposes when date_time is True
        if date_time:
            currentDate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            sheet.update_cell(1, count, 'file_last_updated_on_utc')
            sheet.update_cell(2, count, "{}".format(currentDate))

        # Table data gets inserted
        sheet.update('A2', data.tolist())
