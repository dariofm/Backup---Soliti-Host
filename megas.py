from mega import Mega


mega = Mega()


m = mega.login('dariofm@live.com', 'd35$g')
# login using a temporary anonymous account


#m.delete('CLÍNICA SAÚDE EM VIDA - 1111\CLÍNICA SAÚDE EM VIDA - 1111 07-12-2021 12 horas e 10 min.zip')

files = m.find('CLÍNICA SAÚDE EM VIDA - 1111 07-12-2021 12 horas e 10 min.zip')
if files:
    m.delete(files[0])