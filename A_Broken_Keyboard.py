t = int(input())
for _ in range(t):
    result = ''
    n = input()
    start = 0
    while start < len(n):
        if start+ 1 < len(n) and n[start] == n[start+1]:
            
            start += 2
        else:
            result += n[start]
            start += 1
    print(''.join(sorted(set(result))))