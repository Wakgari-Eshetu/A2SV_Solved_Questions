t = int(input())

for _ in range(t):
    n = input()
    res = [0]*len(n)*2
    for i in range(len(n)):
        res[i] = n[i]
        res[len(res) - i -1] = n[i]
    print(''.join(res))