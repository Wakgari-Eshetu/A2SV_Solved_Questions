n , k = map(int, input().split())
string = input()


value_jump = 1

for i in range(1,n+1):
    if i > value_jump:
        print("NO")
        break 
    if string[i-1] == ".":
        value_jump = max(value_jump, i+k)
    if value_jump >= n:
        print("YES")
        break
else:
    print("NO")
