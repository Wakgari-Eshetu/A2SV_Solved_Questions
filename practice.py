def fun(nums:list) -> int:
    left , middle , right = 0,1,2
    result = 0
    while right < len(nums):
        result = max(result , nums[left]+nums[right]+nums[middle])
        left += 1
        right += 1
        middle += 1
    return result 

array = [1,2,3,4,5,6,7,8,9]
print(f"maximium sum of three consicutive: {fun(array)}")