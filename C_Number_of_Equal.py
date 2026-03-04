from collections import Counter
n , m = map(int , input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count1 = Counter(a)
count2 = Counter(b)
result = 0
for key , value in count1.items():
    if key in count2:
        result += count1[key] * count2[key]
    
print(result)




