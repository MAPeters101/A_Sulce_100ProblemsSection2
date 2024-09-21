import string

letters = string.ascii_lowercase

for letter in letters:
    filepath = f"files/{letter}.txt"
    with open(filepath, 'w') as file:
        file.write(f"{letter}")