from datetime import datetime
from os import listdir
import os
from os.path import isfile, join
import configparser as ini
import sqlite3
from mega import Mega
from spacy import Config
import constants

Constants = constants
    
Conn = sqlite3.connect('C:\\ImplantiSoft\\monitor.db')
Cursor = Conn.cursor()




def logSistema(msg):
    #criando diretório temporarios
    if os.path.exists(Constants.AR'C:\\Kimmera Backup\\Log'):
        pass
    else:
        os.makedirs('C:\\Kimmera Backup\\Log')    
    
    arquivo = open('C:\\Kimmera Backup\\Log\\Kimmera.log','a')
    frases = list()
    frases.append(f'========================================================================\n')
    frases.append(f'Período   : {retornaData()}\n')
    frases.append(f'Ocorrência: {msg}\n')
    arquivo.writelines(frases)  
    arquivo.close()
    print(f'Ocorrência: {msg}\n')


 


def NovoDir(Nome):
    if os.path.exists(Nome):
        pass
    else:
        os.makedirs(Nome)      

def retornaDataArquivo():
    data = datetime.now()
    data_em_texto = data.strftime('%d-%m-%Y %H horas e %M min')
    return data_em_texto
  
def retornaData():
    data = datetime.now()
    data_em_texto = data.strftime('%d/%m/%Y %H:%Mmin')
    return data_em_texto  




def ExcScript():
    NovoDir('C:\\ImplantiSoft\\')
    script = 'C:\\ImplantiSoft\\script.sql'
    sql = '' 
    if os.path.isfile(script):
        arq = open(script)
        linhas = arq.readlines()
        for linha in linhas:
            sql = linha
            Cursor.execute(f"{sql}")
            Conn.commit()            
        arq.close()            
        os.remove(script)     

def SetVersao():
    NovoDir('C:\\ImplantiSoft\\Build\\')
    script = 'C:\\ImplantiSoft\\Build\\versao.sql'
    sql = ''
    if os.path.isfile(script):
        arq = open(script)
        linhas = arq.readlines()
        for linha in linhas:
            sql = linha
        arq.close()            
        os.remove(script)    
    try:
        print(sql)
        if sql != '':
            Cursor.execute(f"{sql}")
            Conn.commit()
            print('Setando Versão do Sistema')
            
    except sqlite3.OperationalError as erro:
        erro = str(erro)
        logSistema(f"'{erro}' - 'Criando tabela PARAM'")
        if erro == 'no such table: PARAM':
            print('Criando tabela PARAM')
            
            Cursor.execute("CREATE TABLE PARAM (ID INTEGER PRIMARY KEY AUTOINCREMENT,VERSAO VARCHAR (3))")
            Conn.commit()
            
            Cursor.execute(f"insert into PARAM (VERSAO) values ('1')")
            Conn.commit()    


def RemoveCaracterInvalido(texto):
    remove_char = "'%$#¨%¨%#$$%$%&3##$*;:�(*/[]\|"
    for x in remove_char:
        texto = texto.replace(x,"")
        
    return texto

