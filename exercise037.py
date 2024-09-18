def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
    words = content.split()
    new_words = []
    for string in words:
        add_words = string.split(',')
        new_words += add_words
    #new_words = [string.split(',') for string in words]
    print(new_words)
    return len(new_words)


print(count_words("words2.txt"))

print("*"*20)

import re
def count_words2(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # pattern = r'[ ,]'
    # words = re.split(pattern, content)
    words = re.split(",| ", content)
    return len(words)


print(count_words2("words2.txt"))



print("*"*20)

def count_words3(filename):
    with open(filename, 'r') as file:
        content = file.read()

    content = content.replace(",", " ")
    words = content.split()
    return len(words)


print(count_words3("words2.txt"))
