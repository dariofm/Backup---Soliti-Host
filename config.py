import configparser as ini

cfg = ini.ConfigParser()
cfg.read('C:\\Kimmera Backup\\Config.ini')
ExcuirBackup = cfg.get('PARAMETRO','Dias')


