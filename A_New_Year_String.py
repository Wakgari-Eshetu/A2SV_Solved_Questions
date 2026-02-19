import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    con_1 = float('inf')
    target = '2026'
    for i in range(n-3):
        ops = sum(1 for j in range(4) if s[i+j] != target[j])
        con_1 = min(con_1, ops )
    
    con_2 = 0
    i = 0
    while i <= len(s) -4:
        if s[i:i+4] == '2025':
            con_2 += 1
            i+= 4
        else:
            i+= 1
    
    print(min(con_1, con_2))