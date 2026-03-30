n = int(input())
string = input()

count_loaf = string.count('L')
count_onion = string.count('O')
count_curr_loaf = 0
count_curr_onion = 0
for k in range(1 , n):
    
    if string[k-1] == 'L':
        count_curr_loaf += 1
    else:
        count_curr_onion += 1
    
    friend_loaf = count_loaf - count_curr_loaf
    friend_onion = count_onion - count_curr_onion
    if count_curr_loaf != friend_loaf and count_curr_onion != friend_onion:
        print(k)
        break
else:
    print(-1)

