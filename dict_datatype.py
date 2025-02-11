"""dictionary datatype"""

"""type of the data"""
a={"course":"python"}
print(type(a))


"""accessing the value using key in dict datatype"""

a={"course":"AIML"}
print(a["course"])


"""printing a dictionary variable"""

a={"name":["neha","sweety","minnu"],"gender":"female","e-mail":["ababbgmail.com","bababgmail.com"]}
print(a)
print(a["name"])
print(a["gender"])
print(a["e-mail"])



"""appending to a dictionary"""

a={"name":["neha","sweety","minnu"]}
a["name"].append("srishanth")
print(a)



"""updating the dictionary's value in a key"""


a={"name":["neha"]}
print(a)
a["name"][0]="sweety"
print(a)


a={"name":["neha","reddy","a"]}
a["name"][2]="addula"
print(a)


a={1:1,2:4,3:9}
b={4:16,5:25,6:36}
c=a.update(b)
print(c)



"""adding a dict to a dict"""

a={"name":{"adhya",'devansh'}}
a["id"]={1,2}
print(a)



"""get keyword for accessing the values in a key"""

a={"name":{"mamatha","jhansi","pavani"}}
print(a.get("name"))


"""none output if we give a key which is not present in the dict"""

a={"name":{"neha","pavani"}}
print(a.get("nme"))     #op=none

a={"name":{"neha","pavani"}}
print(a.get("nme",-1))        #op=-1



"setdefault operation"

#a={"name":{"neha","pavani","mamatha"},"id":"{1,2,3}"}
#print(a.setdefault(country",["india","india","india"]))
#print(a)


"""a.keys(),a.values(),a.items"""

a={"x":[1,2,3,4],"y":[5,6,7,8]}
for ele in a:
    print(ele)


a={"x":[1,2,3,4],"y":[5,6,7,8]}
for ele in a.values():
    print(ele) 


a={"x":[1,2,3,4],"y":[5,6,7,8]}
for ele in a.items():
    print(ele)



"""deleting """

"""1.popitem()"""
test={"a":[1,2,3,4],"b":[5,6,7,8]}
item=test.popitem()                  #deletes the last key-value pair present in the dictionary
print(test,item)        



"""2.pop"""

test={"a":[1,2,3,4],"b":[5,6,7,8]}
item=test.pop("a")                  #deletes the key-value in the dict which is specified by the user
print(test,item)



"""3.del"""
 
#test={"a":[1,2,3,4],"b":[5,6,7,8]}
#item=test.del()
#print(test,item)


"""clear"""

test={"a":[1,2,3,4],"b":[5,6,7,8]}
item=test.clear()
print(test,item)



test={1:1,2:4,3:9}
test.clear
print(test)


""" updating a dictionary """
a={1:1,2:4,3:9}
b={4:16,5:25,6:36}
c=a.update(b)
print(a,c)



"""" del """

test={"a":[1,2,3,4],"b":[5,6,7,8]}
del test["a"]
print(test)




"""zip()"""

a={1:1,2:4,3:9}
for x,y in zip(a.keys(),a.values()):
    print(x,y)


a={'name':['neha','minnu','milky'],"id":[1,2,3]}
for k,v in zip(a.keys(),a.values()):
    print(k,v)



"""copy()"""
d1={1:1,2:4,3:9}
d2=d1.copy()
print(d1,d2)


d1={1:1,2:4,3:9}
d2=d1.copy()        #deep copy
d2[4]=16
print(d1,d2)
  

d1={1:1,2:4,3:9}
d1=d2
d2[4]=16
print("d1:",d1)
print("d2:",d2)
