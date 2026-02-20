n = int(input())
lists = list(map(int, input().split()))

x = sum(lists) // n
for i in range(len(sorted(lists))-1, -1, -1):
    if x >= lists[i]:
        print(lists[i])
        break