while True:
    number = input("Введите число: ")
    # проверяем, что строка - целое положительное число
    if number.isdigit():
        break

# пока длина числа больше 1 цифры
while len(number) > 1:
    # map итерируется по строке, превращая каждый элемент в число
    # результат суммируется и переводится обратно в строку
    number = str(sum(map(lambda x: int(x), number)))
    # number = str(sum([int(i) for i in number]))

print("Сумма цифр:", number)
