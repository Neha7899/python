"""if condition statement"""

"""if-else statement to check which number is greater"""

num1=30
num2=50
if num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")



#num1=int(input("enter num1:"))
#num2=int(input("enter num2:"))
#if num1>num2:
#   print("num1 is greater") 
#else:
#    print("num2 is greater")       



"""if-elif-else condition statement"""

num1=100
num2=100
if num1>num2:
    print("num1 is greater")
elif num1==num2:
    print("num1 and num2 are equal")
else:
    print("num2 is greater")



"""how to know if an element is present in a list"""

a=[10,20,30,40,50]
b=a.count(80)
if(b!=0):
    print("element exists")
else:
    print("element does not exists")    


a=[20,40,50,60,80]
search_element=60
b=a.count(search_element)
if(b!=0):
    print("element exists")
else:
    print("element does not exists")    

"""method 2----in opeartor"""
a=[1,3,5,7,9]
b=8
print(b in a) #op=false
c=5
print(c in a)  #op=true
    


a=[100,200,300,400,500]    
b=800
if b in a:
    print("element exists")
else:
    print('element does not exists')  



a=[20,30,40,50,60]
if(a.count(80)):
    print("element exists") 
else:
    print("element does not exists")         