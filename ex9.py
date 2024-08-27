num_maior = float(input('Entre com o número: '))

for c in range(4):
    numero = float(input('Entre com o número: '))
    if numero > num_maior:
        num_maior = numero
print(f'O maior número é : {num_maior}')
