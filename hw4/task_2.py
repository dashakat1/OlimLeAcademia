def euclid(a, b):
    n = min(a, b)
    a = max(a, b) - min(a, b)
    b = n
    if a == b:
        return a
    else:
        return euclid(a, b)

def check_number(numeral):
    while True:
        num = input(f"Введите {numeral} число: ")
        if num.isdigit():
            break
    return int(num)


num1 = check_number("первое")
num2 = check_number("второе")

print(f"НОД чисел {num1}, {num2}: {euclid(num1, num2)}")
