n , s = map(int, input().split())
a = list(map(int , input().split()))

left , ans = 0 , 0
check_sum = 0
for right in range(n):
    check_sum += a[right]
    while check_sum > s:
        check_sum -= a[left]
        left += 1
    ans = max(ans , right - left + 1)
print(ans) 