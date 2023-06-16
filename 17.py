k = 0
m = -1
a = []
f = open('17 (1).txt')
l = [int(i) for i in f]
for i in range(len(l)):
    if l[i] % 2 == 1:
        a.append(l[i])
s = (sum(a)//len(a))
for i in range(1, len(l)):
    if (l[i-1] % 5 == 0 and l[i] < s) or (l[i - 1] < s and l[i] % 5 == 0):
        k += 1
        m = max(m, l[i-1]+l[i])
print(k, m)
