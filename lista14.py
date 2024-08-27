Nome = input("Insira...")
Idade = float(input("Insira..."))
Salario = float(input("Insira..."))
Sexo = input("Insira...")
EstadoCivil = input("Insira...")

N = len(Nome)


if N > 3:
    print("Nome registrado")

if Idade >= 0 and Idade < 135:
    print("Idade registrada")

if Salario > 0:
    print("Salário registrado")
 
if Sexo == 'f' or Sexo == 'm':
    print("Sexo registrado")
  
if EstadoCivil == 's' or EstadoCivil == 'c' or EstadoCivil == 'v' or EstadoCivil == 'd':
    print("Estado civíl registrado")
