t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    result_check = []

    for i in s:
        if int(i) % 2 != 0:
            result_check.append(i)
        
        if len(result_check) == 2:
            print(result_check[0] + result_check[1])
            break
    if len(result_check) < 2:
        print(-1)
            



    