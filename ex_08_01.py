lst = [1, 2, 3, 4, 5]

def chop(lst):
    del lst [0]
    del lst [-1]

print(lst)

chop(lst)
print(lst)
