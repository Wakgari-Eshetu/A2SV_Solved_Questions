class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        for i,j in zip(sorted(a),sorted(b)):
            if i != j :
                return False 
        return True 