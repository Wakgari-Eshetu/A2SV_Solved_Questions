class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        letvalue = (n*(n+1))//2

        return letvalue - total


       

        