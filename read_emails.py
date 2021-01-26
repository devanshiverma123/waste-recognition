from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv
import os
from upload_dropbox import upload_dropbox
from automate_token import generate_token

class gmailApi(object):
    # account[0] contains the name of the account holder, account[1] contains the path to credentials, account[2] conatins the path to the token
    # in the init function, using fetch_services function, the gmail api service is retrieved, which will then be used further.
    def __init__(self, account):
        self.__user_id='me'
        self.__label_id_one='INBOX'
        self.__label_id_two='UNREAD'
        self.__name = account[0]
        self.__credentials = account[1]
        self.__storage = account[2]
        self.__GMAIL = self.fetch_services(self.__credentials, self.__storage)

    # this function writes the file in the specified location.
    def write_file(self, path, file_data):
        f = open(path, 'wb')
        f.write(file_data)
        f.close()

    # the date and the time of the email is received. Using these names a folder structure is created, to store the attachments from different senders
    def get_date_time(self, header):
        for one in header:
            if one['name'] == 'Date':
                msg_date=one['value']
                date_parse=(parser.parse(msg_date))
                m_date=(date_parse.date())
                m_time = (date_parse.time())
                date_folder=str(m_date)
                time_folder= str(m_time)
                print("The time is:", time_folder)
                return date_folder, time_folder
            else:
                pass
    
    # the name of the sender of the email is returned. This is required to create a folder structure.
    def get_sender(self, header):
        for two in header:
            if two['name'] == 'From':
                msg_from=two['value']
                start=msg_from.find("<")+len("<")
                end=msg_from.find(">")
                sender_folder=msg_from[start:end]
                print("Sender Folder", sender_folder)
                return sender_folder  
            else:
                pass
    
    # if the email is received on a working day, the attachments from that email is stored in the system. The emails received on weekends are filtered out.
    def check_day(self, header):
        for check in header:
            if check['name'] == "Date":
                msg_date=check['value']
                date_parse=(parser.parse(msg_date))
                week_day = date_parse.isoweekday()
                if 0<week_day<6:
                    return True

    # The size of the file is checked, if it exceeds the given size, it will not download.
    def check_size(self, attachment_size):
        print("Attachmnent size", attachment_size)
        if attachment_size<5000000:
            print("Size", attachment_size)
            return True
    
    # The extension of the file is checked. Only the 'csv','txt','jpg','mp4' file will be downloaded.
    def check_extension(self, file_name):
        print("File Name", file_name)
        allowed_formats = ['csv','txt','jpg','mp4']
        if file_name.split('.')[1] in allowed_formats :
            return True
    
    # using the header of the email message, the time,date and the sender of the email sent is retrieved.
    # the folder structure is created. Inside the attachment folder, the date on which the email is sent is specified. 
    # Inside the "date" folder, the "sender" folder exist which contains the email. The file name should be specified as "<time_sent> filename.<extension>"
    def download_attachement(self, service, msg_id, header, download_location):
        try:
            date_folder,time_folder = self.get_date_time(header)
            time  = time_folder.replace(':','-')
            sender_folder = self.get_sender(header)            
            message = service.users().messages().get(userId=self.__user_id, id=msg_id).execute()           

            for part in message['payload']['parts']:
                if(part['filename'] and part['body'] and part['body']['attachmentId']):
                    attachment = service.users().messages().attachments().get(id=part['body']['attachmentId'], userId=self.__user_id, messageId=msg_id).execute()

                    if self.check_extension(part['filename']) and self.check_size(attachment['size']) and self.check_day(header):
                        print(part['filename']," and ", attachment['size'], " authenticated.")
                        file_data = base64.urlsafe_b64decode(attachment['data'].encode('utf-8'))
                        file_loc = time+" "+part['filename']
                        print ("FILE LOC", file_loc)
                        if os.path.exists(os.path.join(download_location,date_folder)):
                            if os.path.exists(os.path.join(download_location,date_folder,sender_folder)):
                                path = os.path.join(download_location,date_folder,sender_folder,file_loc)
                                self.write_file(path, file_data)
                            else :
                                path = os.path.join(download_location,date_folder,sender_folder)
                                os.makedirs(path)
                                path = os.path.join(download_location,date_folder,sender_folder,file_loc)
                                self.write_file(path, file_data)
                        else :
                            os.makedirs(os.path.join(download_location,date_folder))
                            change_path = os.path.join(download_location,date_folder,sender_folder)
                            os.makedirs(change_path)
                            path = os.path.join(download_location,date_folder,sender_folder,file_loc)
                            self.write_file(path, file_data)
                    else:
                        print("Wrong format. Cannot be downloaded.")
                else:
                    print("No body")
                    pass
        except Exception:
            pass
    
    # Using the credentials, the gmail api services are fetched.
    def fetch_services(self, credentials, storage):
        SCOPES='https://www.googleapis.com/auth/gmail.modify'
        store=file.Storage(storage)
        creds=store.get()
        if not creds or creds.invalid:
            #generate token
            generate_token(self.__name)
            flow=client.flow_from_clientsecrets(credentials,SCOPES)
            creds=tools.run_flow(flow, store)    
        GMAIL=discovery.build('gmail','v1',http=creds.authorize(Http()))
        return GMAIL

    # Fetch the new emails. If there are no emails to fetch, nothing is returned.
    def fetch_unread_messages(self):
        unread_msgs = self.__GMAIL.users().messages().list(userId=self.__user_id ,labelIds=[self.__label_id_one, self.__label_id_two]).execute()
        print(unread_msgs)
        try:
            if unread_msgs['resultSizeEstimate'] != 0:
                msg_list = unread_msgs['messages']
                print("total messages",str(len(msg_list)))
                return msg_list
            else: 
                return None
        except Exception as err:
            print("No Message to Download. Error: ", err)

    # Get the location of the where the attachments are to be downloaded.
    # The folder should be in the name "attachments-<account_name>". Return the location.    
    def get_location(self):
        path = str(os.getcwd())
        download_location = os.path.join(path,'attachments-'+self.__name)
        return download_location

    # Once the messages have been read, they should be marked as unread on the gmail account as well.
    def mark_as_read(self, GMAIL, __user_id, m_id):
        GMAIL.users().messages().modify(userId=__user_id,id=m_id,body={'removeLabelIds':['UNREAD']}).execute()

    # Traverse through message list, and download attachments and mark the email as read, if the message list in not empty.
    def traverse_messages(self, msg_list, download_location):
        try:
            for msg in msg_list:
                m_id = msg['id']
                message = self.__GMAIL.users().messages().get(userId=self.__user_id,id=m_id).execute()
                payld = message['payload']
                headr = payld['headers']   
                print("Traverse Messages")
                self.download_attachement( self.__GMAIL, m_id, headr, download_location)
                self.mark_as_read(self.__GMAIL, self.__user_id, m_id)   
            return True
        except Exception as error:
            print("No messages to download.",error)
            return False
    

# get the current file path, and find the absolute path to this file. The accounts contains the record of the emails from which the attachements will be downloaded.
# the storage file contains the unique token to every email address. 
# From one credential, multiple tokens can be created for different users. 
# Once the attachments are downloaded and emails are read, these files are uploaded from the local system to dropbox. 
def main():
    path = __file__
    file_path = os.path.abspath(os.path.join(path, os.pardir))
    account_name = ['ottosero','personal']
    credential_json = "credentials1.json"

    accounts = [['ottosero',os.path.join(file_path,credential_json), os.path.join(file_path, "token", "storage-"+account_name[0]+".json")],
     ['personal',os.path.join(file_path,credential_json), os.path.join(file_path,"token", "storage-"+account_name[1]+".json")]]

    for account in accounts:
        print(account)
        gmail_obj = gmailApi(account)
        msg_list = gmail_obj.fetch_unread_messages()
        path = gmail_obj.get_location()
        if(gmail_obj.traverse_messages(msg_list = msg_list, download_location = path)):
            upload_dropbox(path, r'/attachments-'+account[0])
        else:
            pass


if __name__ == '__main__':
    main() 
