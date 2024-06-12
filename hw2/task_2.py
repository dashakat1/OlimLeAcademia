def reverse_content(file_name):
    # открываем исходный файл
    with open(file_name, "r") as f:
        # создаём итоговый файл
        with open("output.txt", "w") as d:
            # запрашиваются символы, которые будут удалены с правого конца строки
            chars = input("Введите символы, которые хотите удалить: ")
            for line in f.readlines():
                # берём строки без \n, удаляем символы справа, результат переворачиваем
                update_line = line[:-1].rstrip(chars + ";")[::-1]
                # записываем в итоговый файл через \n
                d.write(update_line + "\n")

# пробуем открыть файл input.txt
try:
    reverse_content("input.txt")
# если такого нет, просим пользователя ввести имя другого файла
except FileNotFoundError:
    other_file_name = input("Введите имя существующего файла: ")
    reverse_content(other_file_name)
