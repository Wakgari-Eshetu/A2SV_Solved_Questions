n = int(input())
s = list(input())

count_op = 0
def rec(v:list) -> bool:
    for i in range(0 ,len(v)-2 , 2):
        if s[i] == s[i+1]:
            del(s[i+1])
            count_op += 1
        
        if len(s) % 2 == 1:
            del s[i+2]
            count_op += 1
    return s 
def check(s):
    valid = True
    for i in range(0 , len(s) - 2 , 2):
        if s[i] == s[i+1]:
            valid = False
    if valid and len(s) % 2 == 0:
        return True 

ans = [''.join(s) if check(s) else rec(s)]

    


print(count_op)
print(ans)
        


