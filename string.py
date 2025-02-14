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

s="python,c++,java,go"
s_list=s.split(',')
print(s_list)


s="python c++ java g0"
s_list=s.split()
print(s_list)