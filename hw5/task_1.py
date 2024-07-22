import random

class Planet:

    def __init__(self):
        self.vegetables = 20  # запас растительной пищи
        self.animals = []  # список животных

    def time_lapse(self):

        for animal in self.animals:
            animal.age += 1  # все животные стареют на 1
            if animal.age > animal.lifetime:
                # или умирают и превращаются в растительную пищу
                self.vegetables += animal.size
                self.animals.remove(animal)
                print(f"{animal.name} умер от старости")

            # фаза питания
            if animal.food_base[0] == "plant":
                if self.vegetables > 0:
                    animal.satiety += 26
                    self.vegetables -= 1
                else:
                    animal.satiety -= 9
            else:
                chance = random.choice(["1", "0"])
                if chance == "0":
                    animal.satiety -= 16
                else:
                    prays = [pray for pray in self.animals if pray.name in animal.food_base]
                    if not prays:
                        animal.satiety -= 16
                    else:
                        killed = random.choice(prays)
                        self.animals.remove(killed)
                        animal.satiety += 53
                        print(f"{killed.name} был съеден")

            if animal.satiety > 100:
                animal.satiety = 100
            elif animal.satiety < 10:
                self.animals.remove(animal)
                self.vegetables += animal.size
                print(f"{animal.name} умер от голода")

    def show_animals(self):
        for number, animal in enumerate(self.animals):
            print(number, animal)

    def choose_animal(self, num):
            animal = int(input(f"введите индекс {num} животного: "))
            animal = self.animals[animal]
            if animal.habitat == "air" and animal.age > 3 and animal.satiety > 42:
                return animal
            elif animal.habitat == "water" and animal.satiety > 50:
                return animal
            elif animal.habitat == "land" and animal.satiety > 20 and animal.age > 5:
                return animal
            else:
                print("Это животное не может участвовать в размножении")
                return self.choose_animal(num)

    def create_animals(self, animal):
        if animal.habitat == "water":
            quantity = 10
            sat = 23
        elif animal.habitat == "land":
            quantity = 2
            sat = 73
        else:
            quantity = 4
            sat = 64
        for _ in range(quantity):
            gender = random.choice(["male", "female"])
            new_animal = Animal(animal.name, animal.size, animal.food_base,
                                    animal.habitat, animal.lifetime, gender)
            new_animal.satiety = sat
            self.animals.append(new_animal)
        print(f"На планете {quantity} новых представителей вида {animal.name}!")


    def reproduction(self):
        self.show_animals()
        partner1 = self.choose_animal("первого")
        partner2 = self.choose_animal("второго")
        if partner1.name == partner2.name and partner1.gender != partner2.gender:
            self.create_animals(partner1)
        else:
            print("Это сочетание противоречит законам биологии!")

    def add_animal(self):
        print("Введите...")
        name = input("вид животного: ")
        size = input("размер животного: ")
        food_base = input("кормовую базу животного: ")
        food_base = map(str.strip, food_base.split(","))
        habitat = input("среду обитания животного: ")
        lifetime = input("продолжительность жизни: ")
        gender = input("выберите пол [male/female]: ")
        new_animal = Animal(name, size, food_base,
                            habitat, lifetime, gender)
        self.animals.append(new_animal)

class Animal:

    def __init__(self, name, size, food_base, habitat, lifetime, gender):
        self.name = name
        self.size = size
        self.food_base = food_base  # list
        self.habitat = habitat
        self.lifetime = lifetime
        self.gender = gender
        self.age = 0
        self.satiety = 100

    def __str__(self):
        info = f"{self.name} ({self.habitat}), {self.gender}: {self.age} y.o. Пища: {self.food_base}, сытость: {self.satiety}"
        return info

# START GAME

planet = Planet()

bereshit = [("moon rabbit", 5, ["plant"], "land", 7, "male"),
 ("moon rabbit", 5, ["plant"], "land", 7, "female"),
 ("star wolf", 15, ["moon rabbit", "stray seahorse"], "land", 12, "male"),
 ("star wolf", 15, ["moon rabbit", "stray seahorse"], "land", 12, "female"),
 ("space bee", 2, ["plant"], "air", 5, "female"),
 ("space bee", 2, ["plant"], "air", 5, "female"),
 ("celestial whale", 40, ["space bee"], "air", 20, "female"),
 ("stray seahorse", 3, ["plant"], "water", 10, "female"),
 ("stray seahorse", 3, ["plant"], "water", 10, "male"),
 ("solar bear", 20, ["moon rabbit", "star wolf"], "land", 14, "female")]

for i in bereshit:
     planet.animals.append(Animal(*i))

n = 0
while True:
    command = input("Введите действие:\n"
                    "1 Посмотреть всех особей\n"
                    "2 Добавить новую особь\n"
                    "3 Размножение\n"
                    "4 Моделировать движение времени\n")
    if command == "3":
        planet.reproduction()
    elif command == "4":
        planet.time_lapse()
        n += 1
        print(f"\n{'_'*10} год {n} {'_'*10}")
    elif command == "1":
        planet.show_animals()
    elif command == "2":
        planet.add_animal()
        print(planet.animals)
    elif not planet.animals:
        print("Игра окончена")
        break
    print()
