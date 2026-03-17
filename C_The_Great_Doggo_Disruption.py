from collections import defaultdict
n = input()
s = input()

count = defaultdict(int)
for color in s:
    count[color] += 1
for v in count.values():
    if v >= 2:
        print("Yes")
        break
else:
    print("No")