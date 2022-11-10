url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
print(url)
url_base = url[0:19]
print(url_base)
url_parametros = url[20:]
print(url_parametros)
# usando o método find
print()
print('usando o método find')
# print(url.find('b'))
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# utilizando o método len

parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)
