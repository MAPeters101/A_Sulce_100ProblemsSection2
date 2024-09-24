import glob

letters = []
file_list = glob.glob("files/*.txt")

for filename in file_list:
    with open(filename) as file:
        content = file.read().strip('\n')
    if content in "python":
        letters.append(content)


print(letters)