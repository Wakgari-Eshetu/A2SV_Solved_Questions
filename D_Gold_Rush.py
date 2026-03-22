t = int(input())
for _ in range(t):
    n , m = map(int , input().split())
    def check(n , m):
        check_visted = set()
        
        def ans(x):
            if x == m:
                return True 
            if x < m or x%3 != 0:
                return False 
            if x is check_visted:
                return False 
            check_visted.add(x)
            return ans(x//3) or ans((x*2 )// 3)
        return ans(n)
    
    print('YES' if check(n , m) else 'NO')

