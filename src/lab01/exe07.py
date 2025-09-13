ishod = input()
print("in: " + ishod)
c = ''
for i in range(len(ishod)):
    if ishod[i].isupper():
        cnt = i
        break
c = ''.join([ishod[i] for i in range(cnt, len(ishod), 3)])
print("out:", c)