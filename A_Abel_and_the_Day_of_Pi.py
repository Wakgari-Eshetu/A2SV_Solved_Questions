t = int(input())
for _ in range(t):
    n = input()
    pi = "3141592653589793238462643383279"
    
    count = 0
    leng = min(len(n) , len(pi))
    for i in range(leng):
        if n[i] == pi[i]:
            count += 1
        else:
            break 
    print(count)
    
    