#a=[3,8,5,0,1,9]
#for i in a:
#    if i%2!=0:
#       a.remove(i)
#        a.append(i)
#print(a)   
#in this code it will not work for all test cases check notes

a=[1,3,8,9,5,0]
k=0
for i in a:
    if i%2==0:
        a.remove(i)
        a.insert(k,i)
        k+=1
print(a)
o/p:[8, 0, 1, 3, 9, 5]