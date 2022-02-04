from datetime import datetime
from os import listdir
import os
from os.path import isfile, join
import configparser as ini
import sqlite3
from mega import Mega

   
    
conn = sqlite3.connect('C:\\Kimmera Backup\\cloud.db')
cursor = conn.cursor()

cfg = ini.ConfigParser()
cfg.read('C:\\Kimmera Backup\\Config.ini')



def logSistema(msg):
    #criando diretório temporarios
    if os.path.exists('C:\\Kimmera Backup\\Log'):
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

def SetVersao():
    NovoDir('C:\\Kimmera Backup\\App\\Build\\')
    script = 'C:\\Kimmera Backup\\App\Build\\versao.sql'
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
            cursor.execute(f"{sql}")
            conn.commit()
            print('Setando Versão do Sistema')
            
    except sqlite3.OperationalError as erro:
        erro = str(erro)
        logSistema(f"'{erro}' - 'Criando tabela PARAM'")
        if erro == 'no such table: PARAM':
            print('Criando tabela PARAM')
            
            cursor.execute("CREATE TABLE PARAM (ID INTEGER PRIMARY KEY AUTOINCREMENT,VERSAO VARCHAR (3))")
            conn.commit()
            
            cursor.execute(f"insert into PARAM (VERSAO) values ('1')")
            conn.commit()    


def RemoveCaracterInvalido(texto):
    remove_char = "'%$#¨%¨%#$$%$%&3##$*;:�(*/[]\|"
    for x in remove_char:
        texto = texto.replace(x,"")
        
    return texto



def CountFile(path):
     
    try:
        file = [f for f in listdir(path) if isfile(join(path, f))]
        Count = int(len([f for f in listdir(path) if isfile(join(path, f))]))
    except FileNotFoundError as erro:
        logSistema(erro)

        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)     
            logSistema(f"Criando Diretório Local: '{path}'")       
            file = file = [f for f in listdir(path) if isfile(join(path, f))]
            Count = Count = int(len([f for f in listdir(path) if isfile(join(path, f))]))
    try:
        QuantidadeLocal = int(cfg.get('PARAMETRO','LocalQuantidade'))
    except:
        QuantidadeLocal = 3    
    if Count >= QuantidadeLocal:
        apagar = f'{path}\\{file[0]}'
   
        if os.path.exists(apagar):
            logSistema(f"Limpando excesso de arquivos: '{apagar}'")
            os.remove(apagar)

            
            try:
                cursor.execute('select EMAIL,SENHA from MEGA')
                for i in cursor.fetchall():
                    email = i[0]
                    senha = i[1]
                try:
                    mega = Mega()    
                    mega.login(email, senha)

                except Exception as erro:
                    erro = str(erro)
                    logSistema(erro)
                    pass                  
                
                files = mega.find(str(apagar))
 
                if files:
                    mega.delete(files[0])  
            except TypeError as erro:    
                logSistema(str(erro))
            except Exception as erro:
                erro = str(erro)    
                logSistema(str(erro))

"""mega = Mega()
        
m = mega.login('atomobackups@gmail.com', 'd35$admin')
#m = mega.login('dariofm@live.com', 'd35$g')



m.create_folder('new_folder')"""