n = input()
n2 = len(n) // 2

ms = list()
ms2 = list()


def forr(a):
    for _ in a:
        return _


for i in n[:n2]:
    ms.append(i)
for i2 in n[n2:]:
    ms2.insert(0, i2)

if forr(ms) == forr(ms2):
    print("True")
else:
    print("False")
