import sqlite3
import shutil
from distutils.dir_util import copy_tree
import os
import zipfile
from functions import retornaDataArquivo,CountFile,SetVersao,ExcScript,logSistema
from mega import Mega
from datetime import datetime
import config
#import GoogleDriver

inicio = datetime.now()
    
conn = sqlite3.connect('C:\\Kimmera Backup\\cloud.db')
cursor = conn.cursor()

logSistema(f"********************** Inicio do Processo **********************")

#Executa Scritps
ExcScript()

#Set Versão do Modulo
SetVersao()


cursor.execute('select DESCRICAO,CNPJ from EMPRESA')
for i in cursor.fetchall():
    nome_absoluto =i[0]+' - '+i[1]
    


#criando diretório temporarios
if os.path.exists('C:\\Kimmera Backup\\_tmp'):
    pass
else:
    os.makedirs('C:\\Kimmera Backup\\_tmp')

if os.path.exists('C:\\Kimmera Backup\\upload'):
    pass
else:
    os.makedirs('C:\\Kimmera Backup\\upload')    

#retorna o último caminho do diretório
def trataDiretorio(pasta):
    diretorio = pasta.split('/')
    i = len(diretorio) - 2
    return diretorio[i]
    
#copiar arquivo para a pasta tmp

cursor.execute('select ID,DESCRICAO,TIPO,DIRETORIO from ARQUIVOS')
for i in cursor.fetchall():
    acao    = i[1]
    tipo    = int(i[2])
    arquivo = os.path.basename(acao)
    dir     = i[3]

    if os.path.exists(f'C:\\Kimmera Backup\\_tmp\\{dir}'):
        pass
    else:
        os.makedirs(f'C:\\Kimmera Backup\\_tmp\\{dir}')
    if tipo == 1: 
        print('Copiando Arquivo: '+acao)
        shutil.copyfile(acao,f'C:\\Kimmera Backup\\_tmp\\{arquivo}')
    elif tipo == 0:
        print('Copiando Direitório: '+dir)
        copy_tree(acao, f'C:\\Kimmera Backup\\_tmp\\{dir}\\')
     

#Gera nome do arquivo zip
nome_zip = 'C:\\Kimmera Backup\\upload\\'+nome_absoluto+' '+str(retornaDataArquivo())+'.zip'
print(f'Tratando arquivo: {nome_zip}')
fantasy_zip = zipfile.ZipFile(nome_zip, 'w')
 
for folder, subfolders, files in os.walk('C:\\Kimmera Backup\\_tmp'):
 
    for file in files:
        fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Kimmera Backup\\_tmp'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()


#copiando arquivos para pastas alternativas 
#Sistema Irá apagar arquivos em Ecesso
cursor.execute('select DIRETORIO from DESTINO')
for i in cursor.fetchall():
    destino = i[0]
    #Delete Excesso
    CountFile(destino)
    #Backup Local
    try:
        print('Realizando Backup Local.')    
        shutil.copyfile(nome_zip,destino+'\\'+os.path.basename(nome_zip))
    except FileNotFoundError as erro:
        print(f'Diretório de destino não encontrado: {erro}')
            
  





cursor.execute('select EMAIL,SENHA from MEGA')
for i in cursor.fetchall():
    email = i[0]
    senha = i[1]
    try:
        logSistema('Enviando arquivo para Servidor Mega')
        #Enviando Arquivos 
        mega = Mega()    
        m = mega.login(email, senha)
        m.create_folder(nome_absoluto)
        folder = m.find(nome_absoluto)
        file = m.upload('C:\\Kimmera Backup\\upload\\'+os.path.basename(nome_zip),folder[0])
    except Exception as erro:
        erro = str(erro)
        logSistema(f"Erro ao enviar arquivo Mega '{erro}'")
    


#Enviando Google Driver
#id = GoogleDriver.enviarDriver('C:\\Kimmera Backup\\upload\\'+os.path.basename(nome_zip),'C:\\Kimmera Backup\\upload\\'+os.path.basename(nome_zip))
id = ""

#limpar arquivos antigos
#Gerando Historico 
upArquivo = os.path.basename(nome_zip)
data_envio = datetime.now()

print(f'Arquivo: {upArquivo}\nData: {data_envio}\n')
cursor.execute(f"insert into ARQUIVOS_ENVIADOS (data,arquivo,excluido,DRIVERID) values (CURRENT_DATE,'{upArquivo}','False','{id}')")
conn.commit()

"""
dias = config.ExcuirBackup

#cursor.execute(f"select id,arquivo,DRIVERID from  ARQUIVOS_ENVIADOS where data < date(CURRENT_DATE,'-{dias} day') and excluido = 'False'")
cursor.execute(f"select id,arquivo,excluido,data,DATE('now', '-0 months', '-3 days') data_filtro from  ARQUIVOS_ENVIADOS where  data = DATE('now', '-0 months', '-3 days') and excluido = 'False' ORDER BY id asc LIMIT 3 ")
Total = 0
for arq in cursor.fetchall():
    
    idArq   = arq[0]
    arquivo = arq[1]
    iddriver = arq[2]
    Total = Total + 1
    try:
        print(f'Apagando Backup Antigo: {arquivo}')
        files = m.find(arquivo)
        
        if files:
            m.delete(files[0])  
            #GoogleDriver.deleteDriver(iddriver)
        #Apagando destino local
        cursor.execute('select DIRETORIO from DESTINO')
        for i in cursor.fetchall():
            destino = i[0] 
            print('Apagando arquivo local')     
            if os.path.isfile(destino+'\\'+arquivo):
                print(destino+'\\'+arquivo)
                os.remove(destino+'\\'+arquivo)
    finally:
        cursor.execute(f"update ARQUIVOS_ENVIADOS set EXCLUIDO = '{True}' where id = '{idArq}'")
        conn.commit()
        logSistema(f'Arquivos Deletado: {Total}')
      """      
try:
    shutil.rmtree('C:/Kimmera Backup/_tmp/')
except:
    pass
try:
    shutil.rmtree('C:/Kimmera Backup/upload/')    
except:
    pass    


fim = datetime.now()
tempo =str(fim-inicio)[0:7]
logSistema(f"********************** Fim do Processo: '{tempo}' **********************")
