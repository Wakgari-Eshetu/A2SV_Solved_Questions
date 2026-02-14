import sys
input = sys.stdin.readline

t = int(input())   # remove this line if no multiple test cases

for _ in range(t):  # remove loop if single test case
    n = int(input())

    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    
    print(n)
    print(p)
    print(a)
