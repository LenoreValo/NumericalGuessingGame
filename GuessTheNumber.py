import random

print("Добро пожаловать в числовую угадайку")

# Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100 и False в противном случае.
def isvalid(s):
    if 1 <= int(s) <= 100:
        return True
    else:
        return False

# Функция, реализующая игру
def play_game():
    r = random.randint(1, 100)
    count = 0
    while True:
        num = input("Введите целое число от 1 до 100: ")
        if isvalid(num):
            if int(num) == r:
                print(
                    "Вы угадали, поздравляем!",
                    f"Число совершенных попыток: {count}",
                    sep="\n",
                )
                break
            elif int(num) > r:
                count += 1
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                count += 1
                print("Ваше число меньше загаданного, попробуйте еще разок")
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")


play_game()
while True:
    answer = input("Будете ли еще раз играть? (Да / Нет) ")
    if answer.lower() == "да":
        play_game()
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
