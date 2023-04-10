import random

# Prompt the user to select the range of numbers
print("Добро пожаловать в игру угадай числа!")
print("Выберите диапазон чисел, в котором нужно угадать число:")
start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))
print(f"Хорошо! Число будет выбрано случайным образом в диапазоне от {start} до {end}.")

# Prompt the user to select the difficulty level
print("Выберите уровень сложности:")
print("1. Легкий (10 попыток)")
print("2. Средний (5 попыток)")
print("3. Сложный (3 попытки)")
difficulty = int(input("Введите число, соответствующее уровню сложности: "))
if difficulty == 1:
    max_attempts = 10
elif difficulty == 2:
    max_attempts = 5
elif difficulty == 3:
    max_attempts = 3
else:
    max_attempts = 10

play_again = "д"
best_score = None

while play_again.lower() == "д":
    random_number = random.randint(start, end)
    num_attempts = 0
    guess = None

    print("...")
    print("Поехали!!!")
    print("...")

    while guess != random_number:
        try:
            guess = int(input("Какое ваше предположение: "))
        except ValueError:
            print("Ой! Это не число. Попробуйте еще раз!")
            continue

        num_attempts += 1
        if num_attempts >= max_attempts:
            print(f"Вы превысили максимальное количество попыток ({max_attempts}). Было загадано число {random_number}.")
            break

        if guess < random_number:
            diff = abs(random_number - guess)
            if diff >= 50:
                print("Очень-очень низкое!!!")
            elif diff >= 20:
                print("Очень низкое!!")
            elif diff >= 10:
                print("Немного низкое!")
            elif diff >= 5:
                print("Чуть-чуть ниже (Почти получилось!)")
            else:
                print("Низкое (но очень близко!!)")
        elif guess > random_number:
            diff = abs(random_number - guess)
            if diff >= 50:
                print("Очень-очень высокое!!!")
            elif diff >= 20:
                print("Очень высокое!!")
            elif diff >= 10:
                print("Немного высокое!")
            elif diff >= 5:
                print("Чуть-чуть выше (Почти получилось!)")
            else:
                print("Высокое (но очень близко!!)")

    if guess == random_number:
        if best_score is None or num_attempts < best_score:
            best_score = num_attempts
            print(f"Поздравляю! Вы угадали число {random_number} за {num_attempts} попыток. Новый рекорд!")
        else:
            print(f"Поздравляю! Вы угадали число {random_number} за {num_attempts} попыток.")
            
        play_again = input("Хотите сыграть еще раз? (s/n): ")
        if play_again.lower() == "n":
            print("Спасибо за игру! До новых встреч!")
            break
        elif play_again.lower() != "s":
            print("Неправильный ввод. Игра завершена.")
        break
