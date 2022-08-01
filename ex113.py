import urllib
import urllib.request

site = str(input('Insira um site: '))
try:
    site1 = urllib.request.urlopen("https://"+site+"/")
except urllib.request.URLError:
    print('\033[1;31mO site não está acessível no momento\033[m')
else:
    print('\033[1;32mConsegui acessar o site {} com sucesso!'.format(site))
print(site1.read())