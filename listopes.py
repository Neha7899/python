"""appending a list"""
  
a=[10,20,30,40,50]
a.append(60)
print(a)

b=[10,20,30,40,50]
b.append([60,70,80])
print(b)


"""extending a list"""

a=[1,2,3,4,5]
a.extend([6,7,8])
print(a)

b=[2,4,6,8]
b.extend([10,12])
print(b)


"""inserting an element in a list as per user choice at any place"""

a=[11,22,33,44,55,66]
a.insert(3,43)    #variablename.insert(index,element)
print(a)


b=[12,24,26,48,60]
b.insert(0,2)
print(b)


"""updating an element in a list"""

a=[100,200,300,400,500]
a[1]=150
print(a)

m=[99,88,77,66,55]
m[3]=65
print(m)

x=[3,6,9,12,15,[21,24,27]]
x[5][0]=18
print(x)



"""fetch the element 8 from the following list"""
"""a=[10,20,30,40,50[25[50,60,15[10,8,6]]]]"""

#a=[10,20,30,40,50[25[50,60,15[10,8,6]]]]
#print(a[5][1][3][1])




"""deleting elements from a list"""


"""pop()"""
a=[10,20,30,40,50]
a.pop(1)               #variable.pop(index)
print(a)

"""remove()"""
a=[10,20,30,40,50]
a.remove(30)           #variable.remove(element you want to delete)
print(a)

"""clear()"""
a=[21,31,41,51,61]
a.clear()                #clears the entire list
print(a)



"""how to sort a list(ascending,descending)"""

"""ascending order"""

"""sort()"""
a=[99,77,55,33,11]
a.sort()
print(a)


"""sorted()"""
a=[100,45,23,56,12]
b=sorted(a)
print(b)


a=['r','w','s','y','a']
a.sort()
print(a)


a=['r','w','s','y','a']
b=sorted(a)
print(b)


a=['p','A','w','t','q']
a.sort()                   #based on ASCII values
print(a)


a=['p','A','w','t','q']
b=sorted(a)
print(b)


"""descending order"""

a=[10,45,23,78,65]
b=sorted(a,reverse=True)
print(a)
print(b)

a=[10,45,23,78,65]
b=sorted(a,reverse=False)    #prints ascending orderly
print(b)  

a=[12,24,56,34,89]
a.sort()                                    #ascending orderly
a[::-1]
print(a)



"""index of an element in a list"""
a=[10,20,30,40,50]
a_id=a.index(30)       #gives the index of the given element
print(a_id)



"""count the occurence of an element in a list"""

a=[10,20,30,30,30,20,40,30,50,30]
b=a.count(30)
print(b)

d=a.count(100)
print(d)




"""how to add two given lists"""

l1=[10,20,30]
l2=[40,50,60]
l=list()
l.append(l1)
l.append(l2)
print(l,len(l))




l1=[10,20,30]
l2=[40,50,60]
l=list()
l.extend(l1)
l.extend(l2)
print(l,len(l))




a=[10,20,30]
b=[40,50,60]
c=a+b
print(c)




l=[10,20,30,40,50]
l=l+l
print(l)


