a="neha reddy"
print(a[5])

"""slicing"""

a='nehal reddy'   #positive slicing
print(a[0:4])     #end index is not included


a='nehal reddy'
print(a[-5:-1])     #negative slicing

a="neha reddy"
print(a[0:9:2])     #step size=2. it prints the elements present in 0,2,4,6,8 except end index

print(a[0:10:3])


"""reversing a string"""

a="abcdefg"
print(a[::-1])


""""""
a="cloud"+" "+"camp"
print(a)

a="cloud"*5
print(a)


print("="*20)

print(1,2,sep=" ",end="\n")
print(1,2,sep="/t",end="\n")


"""string formatting"""

a=10
b=20
print("the value of a is {} and the value of b is {}".format(a,b))


x=100
y=500
print("the value of x is {1} and the value of y is {0}".format(x,y))


"""key-value pair"""


sample={"a":10,"b":20}
print("the value of a is {a} and the value of b is {b}".format(a=10,b=20))


"""f-strings"""

sample={"a":100,"b":200}
print(f"the value of a is {sample['a']} and the value of b is {sample['b']}.")



"""string methods"""

"""1.split"""

s="python,c++,java,go"
s_list=s.split(',')           #split
print(s_list)


s="python c++ java g0"
s_list=s.split()
print(s_list)


s="cloud"
s_list=list(s)
print(s_list)

"""2.join"""

s="".join(s_list)           #join
print(s)



""""seperate without string methods"""

sample='a b c'
sep=' '
res=[]
for ch in sample:
    if ch==sep:
        continue
    res.append(ch)
print(res)


sample='a b c'
print(sample.split(" "))


"""3.find"""

a="python,java,c++,go"
print(a.find("c++"))


s="pyhton c++ java"
ans=""
str_search="c++"
str_idx=s.find(str_search)
if str_idx==-1:
    ans="not found"
else:
    ans=str_idx
print(f"{str_search}:",ans)    


"""4.index"""

a="python,java,c++"
print(a.index("java"))
print(a.index("j"))


s="python,java,c++,go"
ans=""
str_search="python"
if str_search in s:
    ans=s.index(str_search)
else:
    ans="not found"
print(f'{str_search}:',ans)




for row in range(5):
    print("*"*(row+1))                  #multiplication on strings


for row in range(5):
    for col in range(5):
        print("*"*(row+1))   
        break 



"""5.count"""

a='a,b,c,d,e,f'   
print(a.count('g'))


"""6.replace"""

a="a,b,c,d,e,f"
a=a.replace("a,b,c","p,q,r")
print(a) 
#type:ignore


"""islower()"""

a="abcdef"
print(a.islower())

"""isupper()"""

a="ABCDEF"
print(a.isupper())


a='a,b,s,G,J'
print(a.isupper())
print(a.islower())

"""capitalize()"""

s="abcDEf"
print(s.capitalize())

"""strip()"""
s="       abc    e        xyz          "
print(s.strip(),len(s))


s="      abc d    efgh"
print(s.lstrip())

s="          abc e          fgh"
print(s.rstrip())




a="abcdef"
s=a.swapcase()
print(s)