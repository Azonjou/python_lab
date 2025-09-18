<h1>Прграммирование и алгоритмизация (Лабараторные)</h1>

<h2>Лабараторная №1:</h2>

**Задание №1:**
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print("Првиет, " + name + "!", "Через год тебе будет " + str(age+1) + ".")
```
![exe1!](/images/lab01/exe1.png)
-------------------------------------------
**Задание №2:**
```python
a = input()
b = float(input())
print("a: " + a.replace('.', ','))
print("b: " + str(b))
print("sum=" + f"{(float(a)+b):.2f}" + ";" + " avg=" + f"{(float(a)+b)/2:.2f}")
print("hhhhh")
```
![exe2!](/images/lab01/exe2.png)
-------------------------------------------
**Задание №3:**
```python
price = int(input())
discount = int(input())
vat = int(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print("База после скидки: " + f"{base:.2f}" + " ₽")
print("НДС: " + f"{vat_amount:.2f}" + " ₽")
print("Итого к оплате: " + f"{total:.2f}" + " ₽")
```
![exe3!](/images/lab01/exe3.png)
-------------------------------------------
**Задание №4:**
```python
m = int(input("Минуты: "))
print(str(m//60) + ":" + f"{(m%60):02d}")
```
![exe4!](/images/lab01/exe4.png)
-------------------------------------------
**Задание №5:**
```python
a, b, c = map(str, input().split())
print("ФИО: ", a, b, c)
print("Инициалы: ", a[0] + b[0] + c[0] + '.')
print("Длина (символов): " + str(len(a) + len(b) + len(c) + 2))
```
![exe5!](/images/lab01/exe5.png)
-------------------------------------------
**Задание №6:**
```python
cheklist = []
tr = fl = 0
for n in range(int(input())):
    data = input().split()

    f = data[0] if len(data) > 0 else ""
    nm = data[1] if len(data) > 1 else ""
    age = data[2] if len(data) > 2 else ""
    bol = data[3] if len(data) > 3 else ""

    cheklist.append([f, nm, age, bol])
for i in range(len(cheklist)):
    print(f"in_{i+1}:", cheklist[i][0], cheklist[i][1], cheklist[i][2], cheklist[i][3])
    if cheklist[i][3] == 'True': tr += 1
    elif cheklist[i][3] == 'False': fl += 1
print("out:", tr, fl)
```
![exe6!](/images/lab01/exe6.png)
-------------------------------------------
**Задание №7:**
```python
ishod = input("in: ")
for i in range(len(ishod)):
    if ishod[i].isupper():
        first_let = i
        break
numbers_list = '0123456789'
for i in range(len(ishod)):
    if ishod[i] in numbers_list and ishod[i+1] not in numbers_list:
        seconf_let = i+1;
        break
distance = seconf_let - first_let
c = ''.join([ishod[i] for i in range(first_let, len(ishod), distance)])
print("out:", c)
```
![exe7!](/images/lab01/exe7.png)
<!-- Код для изображения: ![название файла!](путь к файлу(изображению)) -->
-------------------------------------------
