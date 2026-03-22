a , b = map(int , input().split())

check_sum = []
while b >= a:
    check_sum.append(b)
     
    if b == a:
        check_sum.sort()
        print('YES')
        print(len(check_sum))
        print(*check_sum)
        
    
    if b % 10 == 1:
        b = b // 10
    elif b % 2 == 0:
        b = b // 2
    else:
        break 
else:
    print('NO')
    

