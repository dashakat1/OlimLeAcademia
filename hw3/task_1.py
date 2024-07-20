while True:
    try:
        min_score = int(input("Введите минимальное значение населения в городе: "))
        break
    except ValueError:
        print("Введённое значение не является числом. попробуйте ещё раз!")


with open("cities.txt", "r") as f:
    data = f.readlines()

statistics = sorted([line.strip("\n") for line in data if int(line.split(":")[1]) > min_score])

with open("filtered_cities.txt", "w") as f:
    for city in statistics:
        print(city, file=f)
