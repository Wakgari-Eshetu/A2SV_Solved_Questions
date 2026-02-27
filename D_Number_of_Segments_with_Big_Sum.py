n , s = map(int, input().split())
arr = list(map(int, input().split()))

ans , curr_sum  ,left  = 0 ,0 ,0  
for right in range(n):
    curr_sum += arr[right]

    while curr_sum >= s:
        ans += n - right  
        curr_sum -= arr[left] 
        left += 1
        
print(ans)




