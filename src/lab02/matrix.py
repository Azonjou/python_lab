from function import matr_srt, equal_len
# Exe 1
matrix = [[1, 2], [3, 4]]
if not matrix:
    print("ValueError")
else:
    print(matr_srt(equal_len(matrix)))

# Exe 2

row_sums = [[1, 2], [3]]
if not row_sums:
    print("ValueError")
else:
    if equal_len(row_sums) != "ValueError":
        row_sums = [len(i) for i in row_sums]
        print(row_sums)
    else:
        print("ValueError")

# Exe 3

col_sums = [[1, 2], [3]]
if not col_sums:
    print("ValueError")
else:
    if equal_len(col_sums) != "ValueError":
        col_sums = [sum(row[j] for row in col_sums) for j in range(len(col_sums[0]))]
        print(col_sums)
    else:
        print("ValueError")

