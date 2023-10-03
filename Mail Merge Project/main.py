with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = [line.rstrip() for line in file]

with open("./Input/Letters/starting_letter.txt", mode="r+") as file:
    base_email = file.readlines()
print(base_email)
for name in names:
    with open(f'./Output/ReadyToSend/letter_for_{name}', mode="w") as mail:
        base_email[0] = base_email[0].replace("[name]", f'{name}')
        for content in base_email:
            mail.write(content)
        base_email[0] = base_email[0].replace(f'{name}',"[name]")

print(names)
