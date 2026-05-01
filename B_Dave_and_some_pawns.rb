t = int(input())
for _ in range(t):
    n = int(input())
    enemy_pawns = list(map(int, input()))
    dawit_pawns = list(map(int, input()))
    count = 0
    for i in range(len(dawit_pawns)):
        if dawit_pawns[i] == 0:
            continue 
        if enemy_pawns[i] == dawit_pawns[i]:
            if i == 0 and enemy_pawns[i+1] == 1:
                count += 1
            elif i == len(dawit_pawns)-1 and enemy_pawns[i-1] == 1:
                count += 1
            elif i > 0 and i < len(dawit_pawns)-1 and (enemy_pawns[i-1] == 1 or enemy_pawns[i+1] == 1):
                count += 1
    print(count)
