import string

letters = string.ascii_lowercase

with open("letters044.txt", 'w') as file:
    for i in range(0,26,3):
        file.write(f"{letters[i:i+3]}\n")