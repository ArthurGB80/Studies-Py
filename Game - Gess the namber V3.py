import random

# Prompt the user to select the range of numbers
print("Bem-vindo ao jogo de adivinhação de números!")
while True:
    try:
        start = int(input("Digite o número inicial: "))
        end = int(input("Digite o número final: "))
        if start >= end:
            print("O número inicial deve ser menor que o número final. Por favor, tente novamente!")
        else:
            break
    except ValueError:
        print("Ops! Isso não é um número válido. Por favor, tente novamente!")

print(f"Ok! O número será escolhido aleatoriamente entre {start} e {end}.")

# Prompt the user to select the difficulty level
print("Selecione o nível de dificuldade:")
print("1. Fácil (10 tentativas)")
print("2. Médio (5 tentativas)")
print("3. Difícil (3 tentativas)")
while True:
    try:
        difficulty = int(input("Digite o número correspondente ao nível de dificuldade: "))
        if difficulty not in [1, 2, 3]:
            print("Opção inválida! Por favor, digite um número de 1 a 3.")
        else:
            break
    except ValueError:
        print("Ops! Isso não é um número válido. Por favor, tente novamente!")

if difficulty == 1:
    max_attempts = 10
elif difficulty == 2:
    max_attempts = 5
else:
    max_attempts = 3

play_again = "s"
best_score = None

while play_again.lower() == "s":
    random_number = random.randint(start, end)
    num_attempts = 0
    guess = None

    print("...")
    print("Vamos lá!!!")
    print("...")

    while guess != random_number:
        try:
            guess = int(input("Qual o seu palpite: "))
        except ValueError:
            print("Ops! Isso não é um número. Por favor, tente novamente!")
            continue

        num_attempts += 1
        if num_attempts >= max_attempts:
            print(f"Você excedeu o número máximo de tentativas ({max_attempts}). O número era {random_number}.")
            break

        if guess < random_number:
            diff = abs(random_number - guess)
            if diff >= 50:
                print("Palpite muito muito baixo!!!")
            elif diff >= 20:
                print("Palpite muito baixo!!")
            elif diff >= 10:
                print("Palpite um pouco baixo!")
            elif diff >= 5:
                print("Palpite um pouquinho baixo (Tá quase lá!)")
            else:
                print("Palpite baixo (mas muito próximo!!)")
        elif guess > random_number:
            diff = abs(random_number - guess)
            if diff >= 50:
                print("Palpite muito muito alto!!!")
            elif diff >= 20:
                print("Palpite muito alto!!")
            elif diff >= 10:
                print("Palpite um pouco alto!")
            elif diff >= 5:
                print("Palpite um pouquinho alto (Tá quase lá!)")
            else:
                print("Palpite alto (mas muito próximo!!)")

    if guess == random_number:
        if best_score is None or num_attempts < best_score:
            best_score = num_attempts
            print(f"Parabéns! Você adivinhou que era o número {random_number} usando {num_attempts} tentativas. Novo recorde!")
        else:
            print(f"Parabéns! Você adivinhou que era o número {random_number} em {num_attempts} tentativas. Seu melhor recorde é de {best_score} tentativas.")
            
        play_again = input("Deseja jogar novamente? (s/n): ")
        
        while play_again.lower() not in ("s", "n"):
            print("Resposta inválida. Por favor, digite 's' para jogar novamente ou 'n' para sair.")
            play_again = input("Deseja jogar novamente? (s/n): ")

        if play_again.lower() == "n":
            print("Obrigado por jogar! Até a próxima.")
            break
        elif play_again.lower() == "s":
            # Prompt the user to select the range of numbers
            print("Selecione a faixa de números que você deseja jogar:")
            start = None
            while start is None:
                try:
                    start = int(input("Digite o número inicial: "))
                    if start < 0:
                        raise ValueError
                except ValueError:
                    print("Valor inválido. O número inicial deve ser um número inteiro maior ou igual a zero.")
                    start = None
            end = None
            while end is None:
                try:
                    end = int(input("Digite o número final: "))
                    if end < start:
                        raise ValueError
                except ValueError:
                    print("Valor inválido. O número final deve ser um número inteiro maior do que o número inicial.")
                    end = None

            print(f"Ok! O número será escolhido aleatoriamente entre {start} e {end}.")

            # Prompt the user to select the difficulty level
            print("Selecione o nível de dificuldade:")
            print("1. Fácil (10 tentativas)")
            print("2. Médio (5 tentativas)")
            print("3. Difícil (3 tentativas)")
            difficulty = None
            while difficulty not in (1, 2, 3):
                try:
                    difficulty = int(input("Digite o número correspondente ao nível de dificuldade: "))
                except ValueError:
                    print("Valor inválido. Digite um número entre 1 e 3.")
                    difficulty = None

            if difficulty == 1:
                max_attempts = 10
            elif difficulty == 2:
                max_attempts = 5
            elif difficulty == 3:
                max_attempts = 3

            print(f"Você escolheu o nível de dificuldade {difficulty}. Você terá {max_attempts} tentativas para adivinhar o número.\n")
