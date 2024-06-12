achievements = {}

# открываем файл с оценками
with open("input.txt", "r", encoding="utf-8") as f:
    # проходимся по списку из строк
    for i in f.readlines():
        # ожидаем, что, если мы попытаемся разделить строку по запятой,
        # вернутся имя и оценка
        try:
            name, score = i.strip().split(",")
        # но пропускаем строку, если что-то пошло не так
        except ValueError:
            continue
        name = name.strip()
        # если имена в файле повторяются, добавляем к ключу звёздочку
        while name in achievements.keys():
            name = name + "*"
        # записываем результаты в словарь, оценку переводим в число
        achievements[name] = int(score)

print(achievements)

# суммируем оценки и делим на их количество
average = sum(achievements.values()) / len(achievements)
print("Средняя оценка:", average)

# создаём новый файл
with open("output.txt", "w+", encoding="utf-8") as f:
    # записываем имена студентов, получивших оценку выше средней
    for name, score in achievements.items():
        if score >= average:
            f.write(name.rstrip("*") + "\n")
