# def foo():
#     c = 1
#     return c
# foo()
# print(c)
#

def foo():
    global c
    c = 1
    return c
foo()
print(c)