import string

with open("letters.txt", 'w') as file:
    for char in string.ascii_uppercase:
        file.write(f"{char}\n")