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