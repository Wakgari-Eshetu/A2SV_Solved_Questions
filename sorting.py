lists = [6,3,8,1,5 ]
def bubble_sort(lists):
    for i in range(len(lists)-1):
        for j in range(len(lists)-1-i):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists

print(lists)
lists_1 = bubble_sort(lists)

print()
print(lists_1  )
names = ["Mary","John","Emma"]
heights = [180,165,170]

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    for i in range(len(heights)-1):
        for j in range(len(heights)-1-i):
            if heights[j] < heights[j+1]:
                names[j],names[j+1] = names[j+1], names[j]
        
    return names

print(sortPeople(names, heights))

def selection_sort(lists):
    for i in range(len(lists)):
        min_index = i
        for j in range(i+1, len(lists)):
            if lists[j] < lists[min_index]:
                min_index = j
        lists[i], lists[min_index] = lists[min_index], lists[i]
    return lists

def insertion_sort(lists):
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0 and key < lists[j]:
            lists[j + 1] = lists[j]
            j -= 1
        lists[j + 1] = key
    return lists
def counting_sort(lists):
    
        