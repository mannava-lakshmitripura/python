l=[]
n=int(input("enter no.of elements in the list"))
for i in range(n):
    e=input()
    l.append(e)
print(l)    
l.insert(2,"kamal")
print(l)
l.pop()
print(l)
l.remove('devansh')
print(l)
li=[x.upper() for x in l if "t" in x]    
print(li)    
for i  in range(0,10,1):
    print(i)
#dict key values
keys=['a','b',"c"]
value=[1,2,'3']
dict1=dict(zip(value,keys))
print(dict1)