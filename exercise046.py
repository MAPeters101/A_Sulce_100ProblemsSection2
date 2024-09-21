import string

letters = string.ascii_lowercase
file_letters = []

for letter in letters:
    filepath = f"files/{letter}.txt"
    with open(filepath, 'r') as file:
        file_letters.append(file.read())

print(file_letters)