class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1 , len(nums)):
                if nums[j] > nums[i]:
                    ans[i] = j-i
                    break 
        return ans
        
