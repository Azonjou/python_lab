ishod = input("in: ")
for i in range(len(ishod)):
    if ishod[i].isupper():
        first_let = i
        break
numbers_list = "0123456789"
for i in range(len(ishod)):
    if ishod[i] in numbers_list and ishod[i + 1] not in numbers_list:
        seconf_let = i + 1
        break
distance = seconf_let - first_let
c = "".join([ishod[i] for i in range(first_let, len(ishod), distance)])
print("out:", c)
