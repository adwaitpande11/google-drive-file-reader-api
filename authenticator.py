import json
import os

from google.oauth2 import service_account


class Authenticator:
    SCOPES = ['https://www.googleapis.com/auth/drive']

    def authenticate(self):
        json_content = json.loads(os.environ["SERVICE_ACCOUNT_FILE_CONTENT"])
        return service_account.Credentials.from_service_account_info(json_content, scopes=self.SCOPES)
