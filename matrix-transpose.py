class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row , column = len(matrix ) , len(matrix[0])
        result = [[0]*row for x in range(column)]
        for r in range(row):
            for c in range(column):
                result[c][r] = matrix[r][c]
        return result 

        


        