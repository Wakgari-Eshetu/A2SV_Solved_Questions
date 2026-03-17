from collections import Counter
t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    cost_brand = []

    for _ in range(k):
        b , c = map(int,input().split())
        cost_brand.append([b,c])
    
    count = Counter()
    for b , c in cost_brand:
        count[b] += c
    check_ans = []
    for k , v in count.items():
        check_ans.append(v)
            
    check_ans.sort(key=lambda x : -x)
    ans = 0
    for i in range(n):
        if i  >= len(check_ans):
            break
        ans += check_ans[i]
        
    print(ans)
    

