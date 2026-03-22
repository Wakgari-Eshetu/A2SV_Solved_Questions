k = int(input())
rank = list(map(int , input().split()))


rank.sort()
print(max(0 , rank[-1]-25))