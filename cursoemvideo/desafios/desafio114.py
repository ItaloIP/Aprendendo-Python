import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'Não foi possível conectar no site informado.')
else: 
    print(f'Consegui acessar o site {site}')
    # print(site.read())
