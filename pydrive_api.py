import io

import googleapiclient.discovery
from googleapiclient.http import MediaIoBaseDownload

from authenticator import Authenticator


class PyDriveApi:
    def __init__(self):
        auth = Authenticator().authenticate()
        self.drive = googleapiclient.discovery.build('drive', 'v3', credentials=auth)

    def read_file(self, file_name):
        if file_name == '' or file_name is None:
            raise Exception('Filename cannot be blank or None')

        file = self.fetch_file_metadata_by_name(file_name)
        return self.read_remote_file(file['id'])

    def fetch_file_list(self, q=None):
        return self.drive.files().list(q=q).execute()

    def fetch_file_metadata_by_name(self, file_name):
        file_list = self.fetch_file_list(q="name = '" + file_name + "'")
        if len(file_list) == 0:
            raise Exception('File \'' + file_name + '\' not found')
        return file_list['files'][0]

    def file_list(self, print_to_console=False):
        file_list = self.fetch_file_list(q="'root' in parents and trashed=false")
        if print_to_console:
            for file in file_list:
                print(u'{0} ({1})'.format(file['name'], file['id']))
        return file_list

    def read_remote_file(self, file_id):
        request = self.drive.files().get_media(fileId=file_id)
        byte_io = io.BytesIO()
        downloader = MediaIoBaseDownload(byte_io, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        return byte_io.getvalue().decode("UTF-8")
