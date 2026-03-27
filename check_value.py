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


# linked list DSA 
# 1. singly linked list

class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None


def insert_node_at_end(head , num):
    new_node = Node(num)

    if head is None:
        head = new_node
        
    else:
        temp = head 
        while temp.next:
            temp = temp.next
        temp.next = new_node
      
    return head

head = None

def insert_node_at_begging(head , num):
    new_node = Node(num)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head = new_node 
    
    return head 

def insert_at_any_pos(head , pos , num):
    new_node = Node(num)
    if pos == 1:
        new_node.next = head
        head = new_node

    temp = head
    for i in range(1 , pos-1):
        temp = temp.next
    if temp is None:
        return head
    new_node.next = temp.next
    temp.next = new_node
    return head 

def deletion_from_beg(head):
    if head is None:
        print('linked list is empty |nothing to delete|')
        return head
    temp = head 
    head = temp.next
    del temp 
    return head
def deletion_from_end(head):
    if head is None:
        print('linked list is empty |nothing to delete|')
        return head
    temp = head
    
    if head.next is None:
        return None
    
    while temp.next.next:
        temp = temp.next
    del temp.next.next
    temp.next = None
    return head

def delforanypos(head , pos):
    if head is None:
        print('NOthing to del')
        return head
    temp = head
    if pos == 1:
        head = temp.next
        del temp 
        return head
        
    for i in range(1 , pos-1):
        if temp is None or temp.next is None:
            print('Invalid position')
            return head
        temp = temp.next
    value_to_del = temp.next

    temp.next = value_to_del.next
    del value_to_del
    return head

def print_list(head):
    if head is None:
        print('Nothing to display')
        return head
    temp = head 
    while temp:
        print(temp.data , end= ' ')
        temp = temp.next
    return head

infix = '(A+B)*(C-D)'

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(string:str):
    stack = []
    output = []

    for char in string:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1]!= '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

def infix_to_prefix(string):
    string = string[::-1]
    for ch in string:
        if ch == '(':
            ch = ')'
        elif ch == ')':
            ch = '('
    
    string = ''.join(string)
    postfix = infix_to_postfix(string)

    return postfix[::-1]

def postfix_to_infix(string):
    stack = []

    for ch in string:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"{a}{ch}{b}")
    return stack[-1]

def prefix_to_infix(string):
    stack = []
    string = string[::-1]
    for ch in string:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"{a}{ch}{b}")
    return stack[-1]

def prefix_to_postfix(string):
    stack = []
    for ch in string:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(ch + a + b)
    
    return stack[-1]

def postfix_to_prefix(string):
    stack = []
    for ch in string:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b + ch)
    
    return stack[-1]

def lg(nums):
    max_value = 0
    for i in range(len(nums)):
        count = 0
        for j in range(i , len(nums)-1):
            if nums[j+1] - nums[j] == 1:
                count += 1
        max_value = max(max_value , count )
    return max_value

