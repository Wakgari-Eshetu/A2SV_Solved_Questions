n = int(input())
lists = list(map(int, input().split()))

total = sum(lists)
possible_sum = {0}
for x in lists:
    new_possible_sum = set()
    for s in possible_sum:
        new_possible_sum.add(s + x)
    possible_sum.update(new_possible_sum)

ans = float('inf')
for s in possible_sum:
    ans = min(ans, abs(total - 2 * s))
print(ans)