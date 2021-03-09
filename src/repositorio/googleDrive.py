from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient.http import MediaFileUpload

import os.path
#https://towardsdatascience.com/how-to-manage-files-in-google-drive-with-python-d26471d91ecd


class GoogleDriveRepo: 
    def __init__(self):
        file_name = "mycreds.txt"
        self.gauth = GoogleAuth()
        self.gauth.LoadCredentialsFile(file_name)
        if self.gauth.credentials is None:
            # Authenticate if they're not there
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            # Refresh them if expired
            self.gauth.Refresh()
        else:
            # Initialize the saved creds
            self.gauth.Authorize()
        # Save the current credentials to a file
        self.gauth.SaveCredentialsFile(file_name)
        self.drive = GoogleDrive(self.gauth)

    def uploadFile(self, file_name):
        #print(file_name)
        #folder_id = 'uploaded'
        #f = self.drive.CreateFile({'title': "testing"})
        #f.SetContentFile(file_name)
        #f.Upload()
        #media = MediaFileUpload(file_name, chunksize=-1, resumable=True)
        #self.gauth.service.files().insert(media_body=media, body={'name':'test', 'convert':True})
    
        file = self.drive.CreateFile({'title': 'My Awesome File.txt'})
        file.SetContentString('Hello World!') # this writes a string directly to a file
        file.Upload()
