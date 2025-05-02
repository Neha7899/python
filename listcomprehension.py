l1=[10,20,30,40,50]
l2=[]
for ele in l1:
    l2.append(ele*10)
print(l2)    



#or simply using list comprehension


l1=[10,20,30,40,50]
ans=[ele*10 for ele in l1]
print(ans)



l=['abc','abcde','abcdef']
ans=[len(ele) for ele in l]
print(ans)



"""1.timeit library"""

import timeit
t=timeit.timeit(stmt="""
ans=[]
for ele in range(100):
    ans.append(ele*10)
""",number=1)
print(t)



import timeit
t=timeit.timeit(stmt="""
ans=[]
for ele in range(10):
    ans.append(ele*10)
""",number=1)
print(t)




import timeit
t=timeit.timeit(stmt="""
ans=[ele*10 for ele in range(100)]
""",number=1)
print(t)
                
"""l=[10,15,20,25,30,35,40],output=[10,20,30,40]"""

"""using loops and conditions"""

l=[10,15,20,25,30,35,40]
ans=[]
for ele in l:
    if ele%2==0:
         ans.append(ele)
print(ans)  

"""using list comprehension"""

l=[10,15,20,25,30,35,40]
ans=[ele for ele in l if ele%2==0]
print(ans)


"""using if-else and for in list comprehension"""
l=[10,15,20,25,30,35,40]
ans=[ele if ele%2==0 else None for ele in l]
print(ans)

"""using if-else and for"""
l=[10,15,20,25,30,35,40]
ans=['even' if ele%2==0 else 'odd' for ele in l]
print(ans)



l=[10,15,20,25,30,40,45,50,60]
ans=[ele for ele in l if ele%15==0]
print(ans)