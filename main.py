import urllib.request, json

print("O CNPJ Possui 14 Dígitos! Informe Somente Números!")
cnpj = input("Informe um CNPJ:") #Só aceitar Números

with urllib.request.urlopen(f"https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}") as url:
    dados = json.loads(url.read().decode())


print('Nome Fantasia: ' + dados['NOME FANTASIA'])
print('Razão Social: ' + dados['RAZAO SOCIAL'])
print('CNPJ: ' + dados['CNPJ'])
print('Status: ' + dados['STATUS'])
print('Principais Atividades: ' + dados['CNAE PRINCIPAL DESCRICAO'])
print('Código das Principais Atividades: ' + dados['CNAE PRINCIPAL DESCRICAO'])
print('Data de Abertura: ' + dados['DATA ABERTURA'])
print('======= CONTATO =======')
print('Contato: ' + dados['DDD'] + dados['TELEFONE'])
print('E-mail: ' + dados['EMAIL'])
print('======= ENDEREÇO =======')
print('CEP: ' + dados['CEP'])
print('Estado: ' + dados['UF'])
print('Cidade: ' + dados['MUNICIPIO'])
print('Bairro: ' + dados['BAIRRO'])
print('Nome da Via: ' +  dados['TIPO LOGRADOURO'] + ' ' + dados['LOGRADOURO'])
print('Número: ' + dados['NUMERO'])
print('Complemento: ' + dados['COMPLEMENTO'])
