import random

print("Bem Vindo ao jogo de adivinhar número!!!")
print("...")
print("Estou pensando em um número de 1 a 100! Você pode adivinhar?")
print("...")
print("Pressione ""Enter"" para começar...")
input()
print("...")
print("Vamos lá!!!")
print("...")

play_again = "s"

while play_again.lower() == "s":
    random_number = random.randint(1,100)
    num_attempts = 0
    guess = None

    while guess != random_number:
        try:
            guess = int(input("Qual o seu palpite: "))
        except ValueError:
            print("Oops! Esse não é um número. Por Favor tente novamente!")
            continue
        num_attempts += 1

        if guess < random_number:
            if abs(random_number - guess) >= 50:
                print("O palpite é baixo (muito muito baixo!!!)")
            elif abs(random_number - guess) >= 20:
                print("O palpite é baixo (muito baixo!!)")
            elif abs(random_number - guess) >= 10:
                print("O palpite é um pouco baixo!")
            elif abs(random_number - guess) >= 5:
                print("O palpite está um pouquinho baixo (Tá quase lá!)")
            else:
                print("O palpite é baixo (mas muito próximo!!)")
        
        elif guess > random_number:
            if abs(random_number - guess) >= 50:
                print("O palpite é alto (muito muito alto!!!)")
            elif abs(random_number - guess) >= 20:
                print("O palpite é alto (muito alto!!)")
            elif abs(random_number - guess) >= 10:
                print("O palpite é um pouco alto!")
            elif abs(random_number - guess) >= 5:
                print("O palpite está um pouquinho alto (Tá quase lá!)")
            else:
                print("O palpite é alto (mas muito próximo!!)")

    if num_attempts == 1:
        print("Parabéns!!! Você adivinhou de primeira!!! Demais!!!")
    else:
        print(f"Parabéns! Você adivinhou que era o número {random_number} usando {num_attempts} tentativas.")

    print("Obrigado por jogar!")
    play_again = input("Você quer tentar mais uma vez  (s/n) ")

print("Obrigado por jogar! Até logo!!!")
            
