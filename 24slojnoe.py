k = 1
maxk = 0
maxa = 0
f = open('24.txt').readline()
f = f.split('E')
for i in range(len(f)):
    for x in range(len(f[i])):
        if f[i][x] == 'A':
            maxa += 1
        if maxa > 4:
            if k - 1 > maxk:
                maxk = k - 1
                k = 1
            else:
                k = 1
print(maxk)
