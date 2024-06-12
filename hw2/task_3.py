try:
    # открываем первый файл, считываем список строк
    with open("input1.txt", "r") as f:
        data1 = f.readlines()
# если файла с таким именем не существует
except FileNotFoundError:
    # возвращаем пустой список
    print("Файл input1.txt не существует")
    data1 = []

# то же самое со вторым файлом
try:
    with open("input2.txt", "r") as d:
        data2 = d.readlines()
except FileNotFoundError:
    print("Файл input2.txt не существует")
    data2 = []

# объединяем содержимое двух файлов
data = data1 + data2

# создаём итоговый файл
with open("output.txt", "w") as p:
    # сохраняем отсортированные строки в файл
    for i in sorted(data):
        # удаляем \n, потому что принт их всё равно добавит
        print(i.strip("\n"), file=p)
