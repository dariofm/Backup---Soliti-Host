#atomobackups@gmail.com
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#import pkg_resources.py2_warn
from oauth2client import client
from datetime import datetime

gauth = GoogleAuth()

# Create local webserver and auto handles authentication.
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def enviarDriverAvulso(arquivo,titulo):
    file = drive.CreateFile({'title': titulo})
    file.SetContentFile(arquivo)
    file.Upload()
    return file['id']

def enviarDriver(arquivo,titulo):
    file = drive.CreateFile({'title': titulo[25:]})
    file.SetContentFile(arquivo)
    file.Upload()
    return file['id']


def deleteDriver(id):
    file1 = drive.CreateFile({'id': id})
    file1.Trash()  # Move file to trash.
    file1.UnTrash()  # Move file out of trash.
    file1.Delete()  # Permanently delete the file.

def listFile():
    # Auto-iterate through all files that matches this query
    file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))

    # Paginate file lists by specifying number of max results
    for file_list in drive.ListFile({'maxResults': 10}):
        print('Received %s files from Files.list()' % len(file_list)) # <= 10
        for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id'])) 


def DownloadFile():
    file7 = drive.CreateFile({'id': '1qtJrAaEN0AvHgOsflktuEAC-JHHl-h61'})
    content = file7.GetContentFile('c:\\cupomv2.0\\script.sql')



