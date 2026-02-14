import sys
input = sys.stdin.readline

t = int(input()) 

for _ in range(t):
    n = int(input())
    alice ,bob ,i = 0 ,0 ,0
    array = []
    result = []
    for i in range(1,n+1,4):
        array.append(i)
    summ = 0
    for i in range(len(array)):
        if summ + array[i] > n:
            break
        else:
            result.append(array[i])
        summ += array[i]
    

    result.append(n - sum(result))
    for i in range(len(result)):
        if i%2 == 0:
            alice += result[i]
        else:
            bob += result[i]

    print(alice,bob)
    

        

       
    

  

