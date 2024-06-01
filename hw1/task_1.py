while True:
    # пользователь вводит число строк N
    row_number = input("Введите число строк: ")
    if row_number.isdigit():
        row_number = int(row_number)
        break

for i in range(row_number):
    # число пробелов уменьшается от N до 0
    # число звёздочек увеличивается на 2 с каждым шагом
    final_string = " " * (row_number - int(i + 1)) + "*" * ( 1 + 2 * int(i))
    print(final_string)
