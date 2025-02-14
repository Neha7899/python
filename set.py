a={1,2,2,2,3,4,4,4,5,6,6,6}
print(type(a))
print(a)


a={1,2,3,4,5}
print(a)



"""union"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.union(s2)
print("s3:",s3)



"""intersection"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.intersection(s2)
print("s3:",s3)



"""difference"""

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s1.difference(s2)
print("s3:",s3)

s1={10,20,30,40,50}
s2={40,50,60,70,80}
s3=s2.difference(s1)
print("s3:",s3)




""""deleting"""

"""1.pop()"""

a={1,2,3,4,5,6}
r=a.pop()
print(a,r)
  

"""2.remove()"""

a={10,20,30,40,50}
r=a.remove(30)
print(a,r)


a={10,20,30,40,50}
#r=a.remove(300)     #keyerror becoz element is not present in the set
#print(a,r)

"""3.discard()"""

a={5,6,7,8,9}
r=a.discard(9)
print(a,r)


a={5,6,7,8,9}
r=a.discard(300)
print(a,r)


a={1,2,2,3,4,5,6,6,7}
print(a,type(a))

"""add()"""

a={10,20,30,40,50}
a.add(60)
print(a)


a={10,20,30,40,50}
a.add(10)
print(a)

