n = int(input()) # number of segments we have 
lists = [list(map(int, input().split())) for _ in range(n)] # to make the list of lists 
lists = sorted(lists , key=lambda x :x[0], reverse= True)


for i in range(1,n): 
    if (lists[i-1][0] >= lists[i][0]) and (lists[i-1][1] <= lists[i][1]):
        print(i+1, i )
        break
else:
    print(-1,-1) 
