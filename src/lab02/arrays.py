from function import elem_sort

# Exe 1
min_max = [1.5, 2, 2.0, -3.1]
if len(min_max) != 0:
     # min_max = elem_sort(min_max)
     print(tuple([min(min_max), max(min_max)]))
else:
     print("ValueError")

# Exe 2


unique_sorted = [1.0, 1, 2.5, 2.5, 0]
elements = list(set(elem_sort(unique_sorted)))
elements.sort(reverse=False)
print(elements)

# Exe 3

flatten_elem = [[1, 2], "ab"]
result_sort = []
for i in range(len(flatten_elem)):
    if type(flatten_elem[i]) in [list, tuple]:
        result_sort += list(flatten_elem[i])
    else:
        result_sort = "TypeError"
print(result_sort)


























