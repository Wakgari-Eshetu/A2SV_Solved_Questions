import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n ,m = map(int, input().split())
    array = list(map(int, input().split()))
    max_array_we_have = len(array) + n
    total_sum , count  = 0 , 1
    for i in range(1,max_array_we_have+1):
        if i not in array:
            total_sum += i
            while count <= n :
                if total_sum == m:
                    print("YES")
                    break
                elif total_sum > m:
                    print("NO")
                    break
                count += 1
        
        
    
    
        
        
    

    
    