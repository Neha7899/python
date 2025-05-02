a={"name":["neha","minnu","sweety"]}
print(a["name"])
print(a.get('name'))


a={"name":"neha","id":1,"mail":"abcgmail.com"}
print(a.setdefault("country","india"))
print(a)



a={"name":"neha","id":1,"mail":"abcgmail.com"}
print(a.setdefault("country",["korea"]))
a["country"].append("usa")
a["country"][1]="USA"
print(a)




a=[1,2,3,4,5]
for idx,ele in enumerate(a):
    print (idx,ele)

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
x=a+b+c
y=[a]+[b]+[c]
print(x)
print(y)
print (list(zip(*y)))


l=[1,2,3,4,5]
ans=list(map(lambda x:x*2,l))
print(ans)

