def chop(lst):

    if len(lst) > 2:
        removed = [lst[0], lst[-1]]
        del lst [0]
        del lst [-1]
        return removed

lst = [1, 2, 3, 4, 5]
print(lst)

removed_elements = chop(lst)
print(lst)
print(removed_elements)
