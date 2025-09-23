import urllib
import urllib.request

try:
    url = urllib.request.urlopen("https://www.pudim.com.br/")
    print("Site acessado com sucesso")
except urllib.error.URLError:#exceção padrão
    print("Site indisponivel no momento")