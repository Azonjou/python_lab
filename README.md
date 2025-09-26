<h1>Прграммирование и алгоритмизация (Лабараторные)</h1>

<h2>Лабараторная №2:</h2>

**Задание №1:**
**Пункт №1**
```python
min_max = [1.5, 2, 2.0, -3.1]
if len(min_max) != 0:
     # min_max = elem_sort(min_max)
     print(tuple([min(min_max), max(min_max)]))
else:
     print("ValueError")
```

![exe1_1_1][/images/lab02/exe1_1_1.png]
![exe1_1_2][/images/lab02/exe1_1_2.png]
----------------------------------------------------
**Пункт №2**
```python
unique_sorted = [1.0, 1, 2.5, 2.5, 0]
elements = list(set(elem_sort(unique_sorted)))
elements.sort(reverse=False)
print(elements)
```

![exe1_2_1!][/images/lab02/exe1_2_1.png]
![exe1_2_2!][/images/lab02/exe1_2_2.png]
----------------------------------------------------
**Пункт №3**
```python
flatten_elem = [[1, 2], "ab"]
result_sort = []
for i in range(len(flatten_elem)):
    if type(flatten_elem[i]) in [list, tuple]:
        result_sort += list(flatten_elem[i])
    else:
        result_sort = "TypeError"
print(result_sort)
```

![exe1_3_1!][/images/lab02/exe1_3_1.png]
![exe1_3_2!][/images/lab02/exe1_3_2.png]

--------------------------------------------------------------------
**Задание №2:**
**Пункт №1**
```python
matrix = [[1, 2], [3, 4]]
if not matrix:
    print("ValueError")
else:
    print(matr_srt(equal_len(matrix)))
```

![exe2_1_1!][/images/lab02/exe2_1_1.png]
![exe2_1_2!][/images/lab02/exe2_1_2.png]
----------------------------------------------------
**Пункт №2**
```python
row_sums = [[1, 2], [3]]
if not row_sums:
    print("ValueError")
else:
    if equal_len(row_sums) != "ValueError":
        row_sums = [len(i) for i in row_sums]
        print(row_sums)
    else:
        print("ValueError")
```

![exe2_2_1!][/images/lab02/exe2_2_1.png]
![exe2_2_2!][/images/lab02/exe2_2_2.png]
----------------------------------------------------
**Пункт №3**
```python
col_sums = [[1, 2], [3]]
if not col_sums:
    print("ValueError")
else:
    if equal_len(col_sums) != "ValueError":
        col_sums = [sum(row[j] for row in col_sums) for j in range(len(col_sums[0]))]
        print(col_sums)
    else:
        print("ValueError")
```

![exe2_3_1!][/images/lab02/exe3_3_1.png]
![exe2_3_2!][/images/lab02/exe3_3_2.png]

--------------------------------------------------------------------
**Задание №3:**
```python
tuples = ("Петров Пётр Петрович", "IKBO-12", 5.0)

def format_record(tuple_input):
    """Форматирует входные данные в строку заданного формата

    Функция принимает кортеж с данными студента, проверяет их корректность
    и возвращает отформатированную строку вида "Фамилия И.О., гр. Номер группы, GPA X.XX"

    Args:
        tuple_input(tuple): Кортеж с данными студента в формате:
            -tuple_input[0] (str): ФИО студента (Например: "Иванов Иван Иванович")
            -tuple_input[1] (str): Номер группы (Например: "BIVT-25")
            -tuple_input[2] (float): Средний балл (Например: 4.6)

    Returns:
        str: Отформатированная строка данных студента

    Raises:
        ValueError: Если входные данные некорректны
            - Длина кортежа меньше 3 элементов
            - Имя, Группа или ср. балл пустые
        TypeError: Если входные данные некорректны
            - Ср. балл не является типом данных float

    Examples:
        >>> format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))
        Иванов И.И., BIVT-25, GPA 4.60

        >>> format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))
        Петров П.П., IKBO-12, GPA 5.00
    """
    if len(tuple_input) < 3 or "" in tuple_input[:3]: print("ValueError")
    elif type(tuple_input[2]) != float: print("TypeError")
    else:
        name = tuple_input[0].strip().split()
        name_out = name[0].capitalize() + ' '
        for i in range(1, len(name)):
            name_out += name[i][0].upper() + "."
        print(name_out + ", " + tuple_input[1] + ", " + f"GPA {tuple_input[2]:.2f}")
format_record(tuples)
```

![exe3_1!][D:\Code\Python\Labs\python_lab\images\lab02\exe3_1.png]
![exe3_2!][/images/lab02/exe3_2.png]
----------------------------------------------------------
<!-- Код для изображения: ![название файла!](путь к файлу(изображению)) -->
-------------------------------------------
