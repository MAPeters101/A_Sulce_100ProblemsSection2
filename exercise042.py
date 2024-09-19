a = [1, 2, 3]
b = (4, 5, 6)

for index, value in enumerate(a):
    print(a[index] + b[index])

print("*"*20)
for item in zip(a,b):
    print(sum(item))

print("*"*20)
for i, j in zip(a,b):
    print(i + j)
