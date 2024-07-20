pairs = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}"
        }

def check_brackets(string):
    brackets = []
    for char in string:
        if char in pairs.keys():
            brackets.append(char)
        elif char in pairs.values():
            if char == pairs[brackets[-1]]:
                brackets.pop()
            else:
                break
    if len(brackets) == 0:
        return "True"
    else:
        return "False"


with open("input.txt", "r") as f:
    data = f.readlines()

with open("output.txt", "w") as f:
    for line in data:
        print(check_brackets(line), file=f)
