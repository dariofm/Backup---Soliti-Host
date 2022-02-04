import sqlite3
from mega import Mega
from os import listdir
import os
   
    
conn = sqlite3.connect('C:\\Kimmera Backup\\cloud.db')
cursor = conn.cursor()

def NovoDir(Nome):
    if os.path.exists(Nome):
        pass
    else:
        os.makedirs(Nome) 

def ExcScript():
    NovoDir('C:\\Kimmera Backup\\App\\Build\\')
    script = 'C:\\Kimmera Backup\\App\\Build\\script.sql'
    sql = '' 
  
    if os.path.isfile(script):
        arq = open(script)
        
        linhas = arq.readlines()
        for linha in linhas:
            sql = linha
            cursor.execute(f"{sql}")
            conn.commit()            
        arq.close()            
        os.remove(script)  
ExcScript()