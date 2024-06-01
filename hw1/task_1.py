while True:
    # пользователь вводит число строк N
    row_number = input("Введите число строк: ")
    try:
        int(row_number)
        row_number = int(row_number)
        if row_number > 0:
            break
    except ValueError:
        continue

for i in range(row_number):
    # число пробелов уменьшается от N до 0
    # число звёздочек увеличивается на 2 с каждым шагом
    final_string = " " * (row_number - int(i + 1)) + "*" * ( 1 + 2 * int(i))
    print(final_string)
