from collections import defaultdict
n , k = map(int, input().split())
a = list(map(int , input().split()))

left , longest = 0 , 0
ans_left , ans_right = 0, 0
count = defaultdict(int)
for right in range(n):
    count[a[right]] += 1
    while len(count) > k :
        count[a[left]] -= 1
        if count[a[left]] == 0:
            del count[a[left]]
        left += 1
    
    if right- left + 1 > longest:
        longest = right - left + 1
        ans_left , ans_right = left , right 

print(ans_left + 1 , ans_right + 1)

