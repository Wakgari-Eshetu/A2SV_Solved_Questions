t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    balanced = [False] * n
    zero = one = 0


    for i in range(n):
        if a[i] == '0':
            zero += 1
        else:
            one += 1
        
        if zero == one:
            balanced[i] = True

    flipped = 0
    possible = True

    
    for i in range(n-1, -1, -1):

        current = a[i]

        if flipped:
            current = '1' if current == '0' else '0'

        if current != b[i]:
            if not balanced[i]:
                possible = False
                break
            flipped ^= 1  

    print("YES" if possible else "NO")