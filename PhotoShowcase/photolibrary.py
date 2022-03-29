
from __future__ import print_function
 
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google_auth_oauthlib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd

# Tutorial https://www.youtube.com/watch?v=lj1uzJQnX38 

''' https://developers.google.com/photos/library/reference/rest/v1/albums#Album 
{
  "id": string,
  "title": string,
  "productUrl": string,
  "isWriteable": boolean,
  "shareInfo": {
    object (ShareInfo)
  },
  "mediaItemsCount": string,
  "coverPhotoBaseUrl": string,
  "coverPhotoMediaItemId": string
}

We will need to add SharedAlbumOptions so each student has a collaborative and commentable album with
the teacher given access. 
https://developers.google.com/photos/library/reference/rest/v1/albums#Album.ShareInfo 
{
  "isCollaborative": boolean,
  "isCommentable": boolean
}

A text enrichment is used to identify which trimester and year the student belongs to. 
For example "2022-T1". If more than one instructur is supported, another Enrichment can be used. 
Enrichments can also be locations name and lat,lon where the photo was taken. 
https://developers.google.com/photos/library/reference/rest/v1/albums/addEnrichment 
{
  "enrichmentItem": {
    "textEnrichment": {
        {  "text": string
        }
    }
  }
}
'''

# check for album exists 
def album_exists(creds, name): 
    if search_album_by_name(get_albums(creds), name):
        return True
    else:
        return False

# create a new writeable photo album
def create_photo_library(creds, name):
    if album_exists(creds, name):
        print ("Requested album ", name, " already exists - we don't make duplicates")
        return

    request_body = { 'album': {'title': name, 'isWriteable':True}
    }
    try:
        service = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)
        album = service.albums().create(body=request_body).execute()
        print ("Created new album ", album.get('title'))
    except HttpError as error:
# if student changed their password or revoked our access this would cause errors
        print(f'An error occurred: {error}')

# access ten most recent user files and print the file name and ID
def get_albums(creds):
    try:
        service = build('photoslibrary', 'v1', credentials=creds, static_discovery=False)
        results = service.albums().list(
            pageSize=50, 
        ).execute()
        if results.get('albums') is None:
            print ("\nNo albums found")
            return None
        # First item in our list is the first collection of albums read
        albumList = results.get('albums') 
        nextPageToken = results.get('nextPageToken')
        while nextPageToken:
            # Call the Photos v1 API
            results = service.albums().list(
                pageSize=50, 
                pageToken=nextPageToken
            ).execute()
            albumList.append(results.get('albums'))
            nextPageToken = results.get('nextPageToken')
        
        print ("\r ", len(albumList), " Albums read\r")
        print (albumList)
    # need to delete the token.json file when this happens and try connection again
    # after 12 hours google drops the token and Refresh() fails we don't know why
    except HttpError as error:
        # TODO We need to hndle errors from  API.
        print(f'An error occurred: {error}')
    return albumList

def search_album_by_name(albumList, name):
    for album in albumList:
        if (album.get('title') == name):
            print ("\nFound album ", name, " ID ", album.get('id'))
            return album
    return None
            
