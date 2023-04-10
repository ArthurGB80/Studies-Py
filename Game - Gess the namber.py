print("Olá, Vamos brincar de adivinar um número de 1 a 100?")
print("...")
print("Você tem que adivinhar!!! ... Ok????")
print("...")
print("Pressione ""Enter"" para começar")
input()
print("...")
print("Vamos lá!!!")
print("Essa é sua primeira tentativa")

import random

while True:

    rondom_number = random.radint(1,100)

    attempts = 0

    def get_float_input(prompt):
        while True:
            attempts += 1
            try:
                valor = float(input(prompt)) <= 100
                return valor
            except ValueError:
                print("Valor inválido. Por Favor, digite um número Válido")
                    
    valor1 = get_float_input("Digite um número: ")

    def valor(valor1):
        if valor1 == rondom_number:
            print("Nossa!Parabéns!Você conseguiu de primeira!!!")
            
        elif sum(abs(valor1-abs(rondom_number))) > 50:
            print("Esta longe! Muito Frio")
        elif sum(abs(valor1-abs(rondom_number))) > 20:
            print("Nada mal! Tente mais próximo")

    valor2 = valor

play_again = input("Do you want to play again? (y/n): ")
if play_again.lower() != "y":
    break