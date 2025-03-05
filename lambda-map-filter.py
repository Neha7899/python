add=lambda a,b,c:a+b+c
print(add(1,2,3))
print(add(2,3,c=10))
#print(add(a=2,3,3))     #error-positional arguments follows keyword argument


a=[1,2,3,4,5]
b=[1,2,3,4,5]
ans=[]
for ele1,ele2 in zip(a,b):
    ans.append(ele1+ele2)
    print(ans)



a=[10,20,30,40,50]
b=[10,20,30,40,50]
print(map(lambda ele1,ele2:ele1+ele2,a,b))        #gives a map object
print(list(map(lambda ele1,ele2:ele1+ele2,a,b)))    #typecasting



x=[1,2,3,4,5]
print(list(map(lambda ele:ele+2,x)))

l=1,2,3,4,5
print(list(map(lambda ele:ele*2,l)))


l=1,2,3,4,5
multi=lambda x:x*2
ans=map(multi,l)
print(list(ans))


nums=range(10)
print(list(nums))

x=range(10)
print(list(x))


nums=range(10)
ans=map(lambda x:x%2==0,nums)     #[True, False, True, False, True, False, True, False, True, False]
print(list(ans))



nums=range(10)
ans=filter(lambda x:x%2==0,nums)
print(list(ans))    #filters only true elements 



nums=list(range(10))
ans=map(lambda x:x%2==0,nums)
ans_1=[]
for ele,res in zip(nums,ans):
    if res:
        ans_1.append(ele)
print(ans_1)        



a=['a','b','c','aab','cab','aa']
print(sorted(a))

a=['a','b','c','aab','cab','aa']
print(sorted(a,key=len))