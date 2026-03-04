# D. Black and White Stripe
t = int(input())

for _ in range(t):
    n ,k = map(int, input().split())
    s = input()

    left, count = 0 , 0
    for right in range(n):
        if s[right] == 'W':
            count = right - left + 1
        
        if count == k:
            