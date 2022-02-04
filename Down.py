from mega import Mega
import sqlite3
from zipfile import ZipFile
import os



conn = sqlite3.connect('C:\\Kimmera Backup\\cloud.db')
cursor = conn.cursor()

mega = Mega()


def DownloadMegaArquivos(arquivo):
    cursor.execute('select EMAIL,SENHA from MEGA')
    for i in cursor.fetchall():
        email = i[0]
        senha = i[1]

        mega.login(email, senha)
    print(f'Baixar arquivo: {arquivo}')
    
    file = mega.find(arquivo)
    print(file)
    try:
        mega.download(file)
    except:
        pass   
            
