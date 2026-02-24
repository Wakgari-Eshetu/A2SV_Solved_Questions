n = int(input())
lists = []
for i in range(n):
    lists.append(list(map(int, input().split())))

prev_value = 1000000000000000
for  height , weidth  in lists:
    large_value = max(height , weidth)
    small_value = min(height , weidth)
    if large_value <= prev_value:
        prev_value = large_value
    elif small_value <= prev_value:
        prev_value = small_value 
    else:
        print("NO")
        break   
else:
    print("YES")