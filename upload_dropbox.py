import os
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

def upload_dropbox(local_directory, dropbox_destination):
    TOKEN = 'Iqm59MFX1zsAAAAAAAAAAZAwoWHrcgrXb8gzT4gib4F-_UY770drBCInue79nN7G'
    dbx = dropbox.Dropbox(TOKEN)
    try:
            dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.",err)
    
    # dropbox_destination = r'/attachments'
    for root, dirs, files in os.walk(local_directory):
        for file in files:
            local_path = os.path.join(root,file)
            relative_path = os.path.relpath(local_path, local_directory) 
            dropbox_path = os.path.join(dropbox_destination,relative_path)
            final_dropbox_path = dropbox_path.replace("\\","/")
            print(final_dropbox_path)
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), final_dropbox_path, mute = True)               
            print("Upload Sucessful")