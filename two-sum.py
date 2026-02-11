class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i , val in enumerate(nums):
            tocheck = target - val 
            if tocheck in check:
                return [check[tocheck], i]
            check[val] = i



            
            



        