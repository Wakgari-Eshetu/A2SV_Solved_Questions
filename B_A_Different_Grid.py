t = int(input())
for _ in range(t):
    r , c = map(int, input().split())
    table_a = [[0] for _ in range(c) for _ in range(r)]
    '''for i in range(r):
        for j in range(c):
            table_a[i][j] = map(int, input())'''
    print(table_a)