import dns.resolver as dns
import sys


try:
    lista = ["www.", "webmail.", "mail."]
    alvo = sys.argv[1]
except:
    print("Innapropriate script usage -> dns_resolver.py target")
    sys.exit(1)
for item in lista:
    subdominio = item + alvo
    try:
        resultados = dns.query(subdominio, 'a')
        for resposta in resultados:
            print(subdominio, resposta)
    except:
        pass