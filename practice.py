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

