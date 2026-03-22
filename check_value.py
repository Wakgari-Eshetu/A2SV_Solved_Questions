# selection sort 
arr = [64, 25, 12, 22, 11]

for i in range(len(arr)-1):
    smallest = i  # smallest swap 
    for j in range(i+1 , len(arr)):
        if arr[smallest] > arr[j]:
            smallest = j
    arr[i] , arr[smallest] = arr[smallest] , arr[i]
        

#print(arr)

# insertion sort 

arr = [64, 25, 12, 22, 11]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1

    while j >=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j-= 1
    arr[j+1] = key
print(arr)

arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]

print(arr)

nums = [5, 2, 4, 6, 1, 3]
def merge(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        right_half = nums[mid:]
        left_half = nums[:mid]  

        merge(right_half)
        merge(left_half)

        left , right , ans = 0
        while left < len(left_half) and right < len(right_half):
            if left_half[left] < right_half[right]:
                nums[ans] = left_half[left]
                left += 1
            else:
                nums[ans] = right_half[right]
                right += 1
            ans += 1
        
        while left < len(left_half):
            nums[ans] = left_half[left]
            left += 1
            ans += 1
        
        while right < len(right_half):
            nums[ans] = right_half[right]
            right += 1
            ans += 1
    return nums

print(merge(nums))

# creating the function for quick sort 

nums = [5, 2, 4, 6, 1, 3]
def quick_sort(nums:list)->list:
    if len(nums) <= 1:
        return nums
    else:
        mid = len(nums)//2
        pivot = nums.pop(mid)

        greater_num = []
        smaller_num = []
        for num in nums:
            if num > pivot:
                greater_num.append(num)
            else:
                smaller_num.append(num)

        return quick_sort(smaller_num) + [pivot] + quick_sort(greater_num)

print(quick_sort(nums))

# max heap and using those we can  sort the value 
def heapify(nums , n , i):
    # max heap 
    largest = i
    left = 2*i + 1 
    right = 2*i + 2

    if left < n and nums[left] < nums[largest]:
        largest = left
    if right < n and nums[right] < nums[largest]:
        largest = right
    
    if largest != i:
        nums[i] , nums[largest] = nums[largest] ,nums[i]
        heapify(nums , n , largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n//2 -1 , -1 -1):
        heapify(nums , n , i)
    
    for i in range(n-1 , 0 , -1):
        nums[i] , nums[0] = nums[0] , nums[i]
        heapify(nums , n , 0)
    
    return nums

nums = [5,2,4,6,1,3]
print(heap_sort(nums))
