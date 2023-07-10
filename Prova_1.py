#1) Faça um programa que recebe uma lista de números reais e exibe o seu maior elemento.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(lista1))

#2) Faça um programa que recebe uma lista de números reais e exibe o seu maior elemento.
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
media = sum(lista2) / len(lista2)
print(media)

#3) Dada uma lista de números inteiros, faça um programa que responda a soma de todos os números pares e ímpares.
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_par = 0
soma_impar = 0

for numero in lista3:
    if numero % 2 == 0:
        soma_par += numero
    else:
        soma_impar += numero
        
print(f'Soma de numero impares: {soma_impar}')
print(f'Soma de numeros pares: {soma_par}')

#4) Faça um programa que receba um número e exiba o fatorial desse número.
numero4 = int(input("Digite um número inteiro: "))
fatorial = 1

if int(numero4):
    for i in range(1, numero4 + 1):
        fatorial *= i
else:
    print("Por favor, digite um numero inteiro")
    
print(f"O fatorial de {numero4} é {fatorial}.")

#5) Faça um programa que verifique se uma string possui caracteres duplicados.
lista5 = "Ola mundo, Serasa. Bem-vindo ao Python"

#6 Desenvolva um programa que armazene quatro notas em uma lista e
# que apresente a média final. Caso a média seja igual ou superior a 7,
# apresentar a mensagem "APROVADO", caso contrário, armazenar a
# nota da prova final e recalcular a média. Caso a nova média seja igual
# superior a 5, apresentar a mensagem "APROVADO", caso contrário,
# apresentar a mensagem "REPROVADO"

def caracteres_repetidos(texto):
    repetidos = []
    for letra in texto:
        if texto.count(letra) > 1 and letra not in repetidos:
            repetidos.append(letra)
    return repetidos

result = caracteres_repetidos(lista5)
print("Caracteres repetidos:", result)


def calcular_media(notas):
    return sum(notas) / len(notas)

notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)

if media >= 7:
    print("APROVADO")
else:
    nota_prova_final = float(input("Digite a nota da prova final: "))
    notas.append(nota_prova_final)

    nova_media = calcular_media(notas)

    if nova_media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")


#7 Faça um programa que gere um número inteiro aleatório e que peça
# para o usuário adivinhar, informe se o número que o usuário digitou é
# menor ou maior que o número gerado. O jogo acaba quando o usuário
# acertar o número gerado.

import random

numero_aleatorio = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100

while True:
    numero_digitado = int(input("Digite um número: "))

    if numero_digitado == numero_aleatorio:
        print("Parabéns! Você acertou o número.")
        break
    elif numero_digitado < numero_aleatorio:
        print("O número digitado é menor que o número gerado.")
    else:
        print("O número digitado é maior que o número gerado.")





