def add(numbers, number):
    return numbers.append(number)
def remove(numbers, number):
    return numbers.remove(number)
def replace(numbers, number, number_two):
    idx = numbers.index(number)
    numbers.pop(idx)
    numbers.insert(idx, number_two)
    return 0
def collapse(numbers, number):
    new_numbers = [x for x in numbers if int(x) >= int(number)]
    return new_numbers

numbers = input().split(' ')
command = input()
while command != "Finish":
    if command.startswith("Add"):
        add(numbers, command.split(' ')[1])
    elif command.startswith("Remove"):
        remove(numbers, command.split(' ')[1])
    elif command.startswith("Replace"):
        replace(numbers, command.split(' ')[1], command.split(' ')[2])
    elif command.startswith("Collapse"):
        numbers = collapse(numbers, command.split(' ')[1])
    command = input()
print(" ".join(numbers))