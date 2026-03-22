n , k = map(int, input().split())

s = input()
s = sorted(s)
count , last = 0 , None
ans = 0
for i in range(n):
    if last is None or ord(s[i]) - ord(last)  >= 2:
        ans += ord(s[i] ) - ord('a') + 1
        last = s[i]
        count += 1
    if count == k:
        print(ans)
        break

else:
    print(-1)