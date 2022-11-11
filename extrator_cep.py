import re  # Regular Expression -- RegEx
endereco = "Rua Coronel Romão Sampaio, 651, centro, Moreilândia/PE, 56150-000"
# 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
