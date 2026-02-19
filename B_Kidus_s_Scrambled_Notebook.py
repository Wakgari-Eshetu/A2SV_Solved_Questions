import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = input().strip()
    for i in range(1, len(n)):
        if n[i] != "0" and int(n[:i]) < int(n[i:]):
            print(n[:i], n[i:])
            break 
    else:
        print("-1")