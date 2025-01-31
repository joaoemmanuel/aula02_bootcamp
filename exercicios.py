# #### Inteiros ('int')

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
# resultado_soma = num1+num2
# print("O resultado da soma é:", resultado_soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# CONST_DIV = 5
# num = int(input("Insira um número: "))
# resto = num%CONST_DIV
# print("O resto da divisão é:", resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
# resultado_mult = num1*num2
# print("O resultado da multiplicação é:", resultado_mult)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num1 = int(input("Insira o primeiro número: "))
# num2 = int(input("Insira o segundo número: "))
# resultado_div = num1//num2
# print("O resultado da divisão é:", resultado_div)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num = int(input("Insira o número: "))
# resultado_pot = num**2
# print("O resultado da potenciação é:", resultado_pot)

# #### Números de Ponto Flutuante ('float')

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o segundo número: "))
# resultado_soma = num1+num2
# print("O resultado da soma é:", resultado_soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input("Insira o primeiro número: "))
# num2 = float(input("Insira o segundo número: "))
# media = (num1+num2)/2
# print("O média é:", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Insira a base: "))
# exp = float(input("Insira o expoente: "))
# resultado_pot = base ** exp
# print("O resultado da potência é:", resultado_pot)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Insira a temperatura a ser convertida: "))
# fah = (celsius * 1.8) + 32
# print(f"{celsius}°C equivale a {fah}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#A fórmula para calcular a área do círculo é A = PI * R²
# CONST_PI = 3.14
# CONST_POT = 2
# raio = float(input("Informe o raio do círculo: "))
# area = CONST_PI * (raio**2)
# print(f"A área de um círculo cujo raio é de {raio}cm é de {area}cm")

# #### Strings ('str')

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# texto = str(input("Digite um texto: "))
# print(texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = str(input("Digite seu nome completo: "))
# print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = str(input("Digite uma frase: "))
# print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = str(input("Insira a data no formato DD/MM/YYYY: "))
# dia = data.split("/")[0]
# mes = data.split("/")[1]
# ano = data.split("/")[2]
# print(f"A data informada refere-se ao dia {dia} do mês {mes} do ano {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# frase1 = str(input("Digite sua primeira frase: "))
# frase2 = str(input("Digite sua segunda frase: "))
# print(frase1 + frase2)

# #### Booleanos ('bool')

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# opcao1 = True
# opcao2 = False
# res = opcao1 and opcao2
# print(res)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# opcao1 = True
# opcao2 = False
# res = opcao1 or opcao2
# print(res)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# opcao1 = False
# res = not opcao1
# print (res)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# valor1 = int(input("Informe um valor numérico qualquer: "))
# valor2 = int(input("Informe um valor numérico qualquer: "))
# res = valor1 == valor2
# print(f"Os números são iguais? {res}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1 = int(input("Informe um valor numérico qualquer: "))
# valor2 = int(input("Informe um valor numérico qualquer: "))
# res = valor1 != valor2
# print(f"Os números são diferentes? {res}")

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Insira a temperatura a ser convertida: "))
    fah = (celsius * 1.8) + 32
    print(f"{celsius}°C equivale a {fah}°F")
except ValueError:
    print("Insira um número válido para a temperatura.")
    

# 22: Verificador de Palíndromo


# 23: Calculadora Simples


# 24: Classificador de Números


# 25: Conversão de Tipo com Validação
