#import fdb
import datetime
from datetime import datetime
import sqlite3
from pathlib import Path
import configparser


def trataNomeArquivo():
    conn = sqlite3.connect('C:/Kimmera/data.sl3')
    banco = conn.cursor()
    banco.execute('select id,descricao,chave from tarefa')

    
    now = datetime.now() # current date and time
    hora_backup = now.strftime("%d-%m-%Y %H-%M-%S")
    


    for b in banco.fetchall():
        descicao = b[1].split(" ")
        if len(descicao) > 1:
            nome_composto = descicao[0]+' '+descicao[1]
        elif len(descicao) == 1:
            nome_composto = descicao[0] 
          

        return nome_composto +' - '+ hora_backup
        

 