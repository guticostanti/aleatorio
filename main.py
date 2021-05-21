#Criando uma lista vazia chamada “usuários”
usuarios = []

#Criando um usuário como dicionário com name, username e password
usuario = {
    "name": "Clark Kent",
    "username" : "kent",
    "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
}
# Inclui este usuário na lista usuários
usuarios.append(usuario)

#Criando um usuário como dicionário com name, username e password
usuario = {
    "name": "Bruce Wayne",
    "username" : "wayne",
    "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"
}
# Inclui este usuário na lista usuários
usuarios.append(usuario)

#Criando um usuário como dicionário com name, username e password
usuario = {
    "name": "Christopher Walker",
    "username" : "walker",
    "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"
}

# Inclui este usuário na lista usuários
usuarios.append(usuario)


# Início da atividade
import hashlib

username = input("Digite seu usuário: ")
password = input("Digite sua senha: ")
password = bytes(password, 'utf-8')

crypt = hashlib.sha256()
crypt.update(password)
password = crypt.hexdigest()

autenticado = False

for user in usuarios:
    if (user['username'] == username) and (user['password'] == password):
        autenticado = True
    else:
        continue

if autenticado:
    print(str(user['name']) + " logado!")
else:
    print("Usuário/senha inválidos")







