with open("input.txt", "r") as f:
    data = f.readlines()

groups = {}
for person_data in data:
    parsed_data = person_data.split(":")
    student = parsed_data[0].strip()
    subjects = parsed_data[1].split(",")
    for sub in subjects:
        name = sub.strip().lower()
        try:
            groups[name].append(student)
        except KeyError:
            groups[name] = [student]

while True:
    subject = input("Введите название дисциплины: ").lower()
    if subject in groups.keys():
        break

resp = groups[subject]
print(", ".join(resp))
