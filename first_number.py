a = []
for i in range(8):
    i += 1
    a.append(i)
print(a[::-1], a)


a = list(input())
b = list(input())
c = a
a = b
b = c
print(a, b)