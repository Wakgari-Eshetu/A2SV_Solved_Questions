n = int(input())
lists = list(map(int, input().split()))



print((n*(n+1))//2 - sum(lists))