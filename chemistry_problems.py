user_int = int(input("Введите количество чисел в массиве: "))
count = 0
counter = 0
symbols = 0
while symbols != user_int :
    user = [int(input())]
    symbols += 1
    for i in user:
        if i < 0:
            count += 1
        else:
            counter += 1
print(f"Положительных {counter}, а отрицательных {count}")


user_input = []
count_second = 0
people_second = 0
while people_second != 25:
    user_input = [int(input("Введите 25 чисел: "))]
    for i in user_input:
        people_second += 1
        if i <= 2:
            count_second += 1
print(f"В классе {count_second} отстающих учеников")
