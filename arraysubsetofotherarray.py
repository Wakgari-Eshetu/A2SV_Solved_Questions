#User function Template for python3
from collections import Counter 
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        count1 = Counter(a)
        count2 = Counter(b)
        
        for key in count2:
            if count2[key]>count1[key]:
                return False 
        else:
            return True 
                    
    
    
    
    
