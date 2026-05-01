t = int(input())
for _ in range(t):
    n = int(input())
    enemy_pawns = list(map(int, input()))
    dawit_pawns = list(map(int, input()))
    count = 0
    i = 0
    while i < len(dawit_pawns) - 1:
        if dawit_pawns[i] == 0:
            continue 
        if enemy_pawns[i] == 0:
            count += 1
            i += 1
        
        if enemy_pawns[i] == 1 and  dawit_pawns[i] == 1:
            if i == 0 and enemy_pawns[i+1] == 1:
                count += 2
                i += 2 
            elif i>0 and i <len(dawit_pawns) and enemy_pawns
        
            
        
    
    print(count)
