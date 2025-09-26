from function import matr_srt, equal_len
# Exe 1
def transpose(matrix):
    if not matrix:
        raise ValueError
    else:
        return matr_srt(equal_len(matrix))
print(transpose([[1, 2], [3, 4]]))

# Exe 2

def row_sums(col_row_sums):
    if not col_row_sums:
        raise ValueError
    else:
        if equal_len(col_row_sums) != "ValueError":
            col_row_sums = [sum(i) for i in col_row_sums]
            return col_row_sums
        else:
            raise ValueError
print(row_sums([[1, 2, 3], [4, 5, 6]]))
# Exe 3

def col_sums(sums_cls):
    if not sums_cls:
        raise ValueError
    else:
        if equal_len(sums_cls) != "ValueError":
            sums_cls = [sum(row[j] for row in sums_cls) for j in range(len(sums_cls[0]))]
            return sums_cls
        else:
            raise ValueError
print(col_sums([[-1, 1], [10, -10]]))

