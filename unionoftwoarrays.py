class Solution:    
    def findUnion(self, a, b):
        a = set(a)
        for i in b:
            if i not in a:
                a.add(i)
        
        return sorted(a)