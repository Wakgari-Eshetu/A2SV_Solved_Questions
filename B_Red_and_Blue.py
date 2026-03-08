t = int(input())
for _  in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))

   
    prefix_r = 0
    ans = 0
    for num in r:
        prefix_r += num
        ans = max(ans ,prefix_r )
    
    
    prefix_b = 0
    ans_b = 0
    for num in b:
        prefix_b += num
        ans_b = max(ans_b , prefix_b)
    
   
    print(ans+ans_b)

        
    