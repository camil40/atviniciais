n = input('Insira o nome de usuário: ')
s = input('Insira a senha: ')
while n == s:
    print("Erro! A senha não pode ser igual ao nome de usuário")
    n = input('Insira o número de usuário: ')
    s = input('Insira a senha: ')
print("Usuário cadastrado")


