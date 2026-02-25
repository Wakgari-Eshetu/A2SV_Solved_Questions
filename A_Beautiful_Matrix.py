l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))
l4 = list(map(int, input().split()))
l5 = list(map(int, input().split()))

matrix = [l1, l2, l3, l4, l5]

for row_index, row in enumerate(matrix):
    if 1 in row:
        col_index = row.index(1)
        if row_index == 0 or row_index == 4:
            if col_index == 0 or col_index == 4:
                print(4)
            elif col_index == 1 or col_index == 3:
                print(3)
            else:
                print(2)
        elif row_index == 1 or row_index == 3:
            if col_index == 0 or col_index == 4:
                print(3)
            elif col_index == 1 or col_index == 3:
                print(2)
            else:
                print(1)
        else:  
            if col_index == 0 or col_index == 4:
                print(2)
            elif col_index == 1 or col_index == 3:
                print(1)
            else:
                print(0)
        break  