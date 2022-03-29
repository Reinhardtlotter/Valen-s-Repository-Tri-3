from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import httplib2

from photolibrary import create_photo_library, get_albums, search_album_by_name

# Instructions to create API credentials on Google Cloud 
# Download the client secret and name it "credentials.json" file in our project
# Our program will create token.json for a user after we do a successful connect
# https://www.youtube.com/watch?v=pBVAyU4pZOU 

# If modifying these scopes, delete the file token.json.
# this is read-only but will need write and delete soon
#SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
# this gives full access to drive metadata and photoslibrary 
SCOPES = ['https://www.googleapis.com/auth/drive.metadata',
        'https://www.googleapis.com/auth/photoslibrary']


def authenticate():
    """ 
     Our test prints the names and ids of the first 10 google drive files recently accessed.
     We would use the IDs later to retrieve images
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if creds is None or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # been having trouble after token expires with refresh token; might need to force refresh token
            # workaround is to regenerate the secrets in Google Cloud Del Norte account
            # maybe just forcing the user to refresh will work, or deleting the token.json?
            # tried this in credentials.json but google said the & is not allowed
            # https://accounts.google.com/o/oauth2/auth?access_type=offline&approval_prompt=force'
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
    

# access ten most recent user files and print the file name and ID
def access_gdrive_files(creds):
    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO We need to hndle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    creds = authenticate()
    # practice reading google drive files - not sure if we need to use this
    access_gdrive_files(creds)
     
    create_photo_library(creds, "Valen-2022-Showcase")
    albumList = get_albums(creds)
    album = search_album_by_name(albumList, "Valen-2022-Showcase")

