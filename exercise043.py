import string

letters = string.ascii_lowercase
#print(letters)
with open("letters043a.txt", 'w') as file:
    for index in range(0,25,2):
        file.write(f"{letters[index]}{letters[index+1]}\n")

print("*"*20)
odd_letters = string.ascii_letters[0:26:2]
even_letters = string.ascii_letters[1:26:2]
with open("letters043b.txt", 'w') as file:
    for i, j in zip(odd_letters, even_letters):
        file.write(f"{i}{j}\n")