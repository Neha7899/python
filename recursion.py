"""sum of first three natural numbers"""
 
def f1(n):                       #3+2+1=6
    if n==1:
        return 1
    s=n+f1(n-1)
    return s
ans=f1(3)
print(ans)


def f(n):                       #1+2+3=6
    if n==3:
        return 3
    s=n+f(n+1)
    return s
ans=f(1)
print(ans)


"""sum of first 100 natural numbers"""

"""recursive approach"""

def f(n):
    if n==100:
        return 100
    s=n+f(n+1)
    return s
ans=f(1)
print(ans)


def z(n):
    if n==1:
        return 1
    s=n+z(n-1)
    return s
ans=z(100)
print(ans)

"""loop-based approach"""

ans=0
for num in range(1,101):
    ans+=num
print(ans)   



"""factorial of a number"""

def fact(n):
    if n==1:
        return 1
    s=n*(n-1)
    return s
ans=fact(5)         #assigning input in the program itself
print(ans)



def fact(n):
    if n==1:
        return 1
    s=n*(n-1)
    return s
n=int(input("enter a number:"))            #taking the input from the user
ans=fact(n)
print(ans)