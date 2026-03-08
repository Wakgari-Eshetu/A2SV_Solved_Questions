# c.Not a cheap string 
t = int(input())
for _ in range(t):
    w = input()
    p = int(input())
    dicts = {
        'a':1 , 'b': 2 , 'c':3 ,'d':4 ,'e':5 ,'f':6 ,'g':7 ,'h':8
        ,'i':9 ,'j':10,'k':11 ,'l':12 ,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20
        ,'u':21,'v':22,'w':23 ,'x':24 ,'y':25,'z':26    }
    check_sum = 0
    w = list(w)
    for i in w:
        check_sum += dicts[i]
    
    while check_sum > p:
        max_value = max(w , key=lambda x: dicts[x])
        check_sum -= dicts[max_value]
        w.remove(max_value)
    print(''.join(w))

