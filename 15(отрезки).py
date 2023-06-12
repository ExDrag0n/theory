P = [i for i in range(5, 31)]
Q = [i for i in range(14, 24)]
ans = []
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        flag = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
             if not(((x in P) == (x in Q)) <= (not(x in A))):
                 flag = 0
                 break
        if flag == 1:
            ans.append(len(A))
print(max(ans))
