#a='u'       numeric datatypes:int,float,complex
#print(type(a))
#O/P: <class 'str'>
#a=3+4j
#print(type(a))
#sequence datatypes:string

#list:dynamic size,mutable
#a = []
#print(type(a))     o/p:<class 'list'>

#a=[1,2,"sai",6.7,True]
#print(a[1])  o/p:2

#a=[1,2,"sai",6.7,True]
#a[2]="abc"
#print(a[2]) o/p:abc

#a=[1,2,4.5,True]
#a[7]="hi"
#print(a)   o/p:IndexError: list assignment index out of range


#for dynamic storage of list use append keyword(only it adds/creates only one object?group)
#a=[1,2,"sai",6.7,True]
#a.append("ab")
#print(a)  o/p:[1, 2, 'sai', 6.7, True, 'ab']

#a=[1,2,"sai",6.7,True]
#a.append(["ab",5,6])
#print(a)  
#o/p:[1, 2, 'sai', 6.7, True, ['ab', 5, 6]]

#extend use to add n no.of objects or groups
#a=[1,2,7.9,True,"hi"]
#a.insert(3,5)
#print(a)
#pop:last object should deleted

#remove:delete any object
#a=[1,"hi",True,9.0]

#print(a.remove("hi"))
#print(a)
#tuple:(),immutable
#a=(2,6.9)
#a[0]=1           o/p:TypeError: 'tuple' object does not support item assignment
#print(a)

#string:immutable,ordered/sequence data type
#a="sai"
#a+="hi"
#print(a) o/p:saihi
#a="abcdef"
#a="lfhf"
#print(a) o/p:lfhf
#set:unordered data type,allows different data types,
#don't have any indexes,no sequence,not able to print individual object
#set doesn't allow duplicates(ex:8,8.0 it will print 8 only)
#set is mutable:it will add & remove the   objects
#a={5,8.9,"hi"}
#print(type(a))   o/p:<class 'set'>
#a={3,79}
#print(a[0])   0/p:TypeError: 'set' object is not subscriptable

#a={False,0,1,True}
#a.add("abc")
#print(a)       o/p:{False, 1, 'abc'}
#a={False,0,1,True}
#a.discard(1)
#print(a)  o/p:1

#a={False,0,1,True}
#a.discard(8) here 8 value isn't there so it doesn't give error,,if it have 8 it will remove 8
#print(a)  o/p:{False, 1}

#a={False,0,1,True}
#a.remove(9)   here it will show error(since 9nvalue not there)
#print(a)   o/p:KeyError: 9
#a={} dictionary contains set and value
#print(type(a))  o/p:<class 'dict'>

#a={6} it has only values
#print(type(a))  o/p:<class 'set'>
#a=set()  used to print empty set
#print(type(a)) o/p:<class 'set'>
#dictionary:mutable,unordered,individuals are displayed,no duplicates
#a={1:"def" , 2:"abc" ,3:"jfhgdvh"}
#print(a[1])  o/p:def
#a={1:"def" , 2:"abc" ,2:"jfhgdvh"}  o/p:{1: 'def', 2: 'jfhgdvh'}
#print(a)  because,it updates 
#a={1:"def" , 3:"abc" ,2:"jfhgdvh"}

#print(a.items()) o/p:
#dict_items([(1, 'def'), (3, 'abc'), (2, 'jfhgdvh')])
#a={1:"def" , 3:"abc" ,2:"jfhgdvh"}
#print(a.values()) o/p:dict_values(['def', 'abc', 'jfhgdvh'])