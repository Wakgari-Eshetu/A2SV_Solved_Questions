t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = float('inf')

    for i in range(n):
        
        if i + 1 < n and s[i] == 'a' and s[i+1] == 'a':
            ans = 2

        if i + 2 < n and s[i] == 'a' and s[i+2] == 'a':
            ans = min(ans, 3)

        if i + 3 < n and s[i] == 'a' and s[i+3] == 'a' and s[i+1] != s[i+2]:
            ans = min(ans, 4)

        if i + 6 < n:
            sub = s[i:i+7]
            if sub.count('a') == 3 and sub.count('b') == 2 and sub.count('c') == 2:
                if sub[0] == 'a' and sub[-1] == 'a':
                    ans = min(ans, 7)

    print(ans if ans != float('inf') else -1)