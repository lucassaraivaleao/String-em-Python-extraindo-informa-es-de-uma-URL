import re  # Regular Expression -- RegEx
endereco = "Rua Coronel Romão Sampaio, 651, centro, Moreilândia/PE, 56150-000"
# 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

#-------------------------------------------------------------------------------------
# Extração de cpf dentro de uma string
dados_usuario = "Lucas Saraiva Leão, analista de sistemas, cpf: 123.456.789-00"
modelo_cpf = re.compile("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}")
buscar_modelo = modelo_cpf.search(dados_usuario)
if buscar_modelo:
    cpf = buscar_modelo.group()
    print(cpf)
    