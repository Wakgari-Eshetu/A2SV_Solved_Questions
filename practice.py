class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]
        
h = HashTable(10)

dict_ = {"name":"John", "age":30, "city":"New York"}
rev_dict = {v:k for k, v in dict.items()}


d = {1:"one", 2:"two", 3:"three", "age":30}
lists = ["one", "two", "three", "four"]
#d = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
d = dict()
for x in enumerate(range(2)):
    d[x[0]] = x[1]
    d[x[1]+7] = x[0]
print(d)

d = dict()
for x in enumerate(range(3,5)):
    d[x[0]] = x[1]
    d[x[1]+7] = x[0]
print(d) 
        
d = {} 

def addTodict(country): 
	if country in d: 
		d[country] += 1
	else: 
		d[country] = 1

addTodict('China') 
addTodict('Japan') 
addTodict('China') 

print (len(d))

sq_of_numbers = {x:x**2 for x in range(1,8)}
print(sq_of_numbers)

# if we want to create a dictioanry from to different lists 
# their length should be same
keys = ["name", "age", "city"]
values = ["John", 30, "New York"]
my_dict = { k:v for k,v in zip(keys,values)}
print(my_dict)

d = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(d)