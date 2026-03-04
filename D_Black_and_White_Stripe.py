# D. Black and White Stripe
t = int(input())

for _ in range(t):
    n ,k = map(int, input().split())
    s = input()

    white_count = 0 
    for i in range(k):
        if s[i] == 'W':
            white_count += 1
    value = white_count

    for i in range(k, n):
        if s[i-k] == 'W':
            white_count -= 1
        if s[i] == 'W':
            white_count += 1
        value = min(value , white_count)

    print(value)
