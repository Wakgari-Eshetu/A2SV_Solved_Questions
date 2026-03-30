t = int(input())
for _ in range(t):
    n = int(input())
    lists = list(map(int, input().split()))
    
    counter = {}
    for x in lists:
        counter[x] = counter.get(x, 0) + 1
    ans = 0
    for key, value in counter.items():
        ans += value // 3
    print(ans)