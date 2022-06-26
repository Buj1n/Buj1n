def replace(messages, message, editedVersion):
    idx = messages.index(message)
    messages.pop(idx)
    messages.insert(idx, editedVersion)
    return 0

def pin(messages, message):
    for z in messages:
        if z == message:
            messages.remove(message)
            messages.append(message)

def add_spam(spam):
    for n in spam[1::]:
        messages.append(n)

command = input()
messages = []
while command != "end":
    if command.startswith("Chat"):
        messages.append(command.split(' ')[1])
    elif command.startswith("Delete"):
        for x in messages:
            if x == command.split(' ')[1]:
                messages.remove(command.split(' ')[1])
    elif command.startswith("Edit"):
        replace(messages, command.split(' ')[1], command.split(' ')[2])
    elif command.startswith("Pin"):
        pin(messages, command.split(' ')[1])
    elif command.startswith("Spam"):
        spam = command.split(' ')
        add_spam(spam)
    command = input()

print("\n".join(messages))