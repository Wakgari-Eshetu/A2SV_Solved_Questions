n = int(input())
lists = list(map(int, input().split()))


lists.sort()
ans = lists[((n-1)//2)]
print(ans)
    


