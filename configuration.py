import json


class Configuration:
    ''' Configuration has the responsiblity of managing loading
        data and credentials for a task
    '''

    def __init__(self, task_path):
        ''' __init__ loads 'credentials.json' of a task
        
            Sets properties:
                @task_dir: 
                    type: str
                    description: path of task directory
                @json_object:
                    type: object
                    description: json object of credentials.json
                    file: credentials.json
                    requires keys: 'sheet_id' - 'google-credentials'
        '''
        self.task_dir = "tasks/{}".format(task_path)

        with open("{}/credentials.json".format(self.task_dir)) as json_file:
            self.json_object = json.load(json_file)

    def getSheetId(self):
        ''' Retrieves Google sheet Id of a task
        
            Note:
                Google Sheet Id can be retrieved from URL
                The '{}' in the URL is the location of the Sheet id
                https://docs.google.com/spreadsheets/d/{}/edit#gid=0
        
            @Returns:
                str : Google sheet id
        '''
        return self.json_object["sheet_id"]

    def getGoogleCredentials(self):
        ''' Retrieves Google Service account credentials of the Google Sheet API

            Requirement:
                - Google Sheets API & Google Drive API must be enabled
                    https://console.cloud.google.com/apis/dashboard
                - Google Sheets API Service Account generated
                    -> https://developers.google.com/workspace/guides/create-credentials#create_a_service_account
                    -> https://developers.google.com/workspace/guides/create-credentials#obtain_service_account_credentials
                - 'client-email' shared with Google Sheet
        
            @Returns:
                object: Returning object of account service credentials
                    str: 'type'
                    str: 'project_id'
                    str: 'private_key_id'
                    str: 'private_key'
                    str: 'client_email'
                    str: 'client_id'
                    str: 'auth_uri'
                    str: 'token_uri'
                    str: 'auth_provider_x509_cert_url'
                    str: 'client_x509_cert_url'
        '''
        return self.json_object["google-credentials"]

    def getGoogleScopes(self):
        return [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]

    def getMySqlCredentials(self):
        ''' Retrieves MySql credentials for database
        
            @Returns:
                object: Returning object of MySql credentials
                    str: 'host'
                    str: 'user'
                    str: 'auth_plugin'
                    str: 'password'
                    str: 'database'
        '''
        with open("configurations/db-credentials.json") as json_file:
            return json.load(json_file)

    def getQuery(self):
        return open("{}/query.sql".format(self.task_dir)).read().replace('\n', ' ')
