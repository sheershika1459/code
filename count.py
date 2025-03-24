a=[1,0,2,1,1,2,2,2]
dict = {}
for i in a:
    if i in dict:dict[i]+=1
    else:  dict[i]=1  
print(dict)

o/p:{1: 3, 0: 1, 2: 4}