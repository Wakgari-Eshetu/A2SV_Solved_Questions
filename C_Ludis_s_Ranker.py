n  = int(input())
arr = [int(i) for i in input().split()]
position = []
 
for i in range(n): 
    count = 0
    for j in range(n): 
        if arr[i] < arr[j]:
            count += 1 
    position.append(count + 1) 
 
print(*position) 

"hello"[1]