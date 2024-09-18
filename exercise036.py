def words_count(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return len(content.split())

print(words_count("words1.txt"))