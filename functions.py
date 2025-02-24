"""takes nothing and returns nothing"""

def add():
    print(2+5)
    print(2+3)
add()


"""takes something and returns nothing"""

def add(a,b):
    print(a+b)
add(9,1)


def sub(a,b):
    print(a-b)
sub(3,5)



def sub(a,b):
    print(a-b)
sub(b=10,a=5)
sub(a=10,b=5)


"""takes something and returns something"""

def add(a,b):
    ans=a+b
    return ans
res=add(55,5)
res=res+10
print(res)

def add(a,b):
    return a+b
ans=add(a=3,b=10)
print(ans)


def add(a,b,c=10):
    return a+b+c
res=add(2,3)
print(res)



def add(a,b,c=10):
    return a+b+c
res=add(a=2,b=10)
print(res)



def add(a,c,b):
    return a+b+c
res=add(3,7,5)
print(res)



def add(a,b,c=20):
    return a+b+c
res=add(10,b=10,c=20)
print(res)



def linear_search(given_list,search_element):        #defining a funtion
    for idx,ele in enumerate(given_list):
        if ele==search_element:
            return True,idx
        return False,-1
given_list=[1,2,3,4,5]
search_element=[5]
res=linear_search(given_list,search_element)          #calling a function
print(type(res))
print(res)




def add(a,b):
    return a-b
res=add(1,b=3)
print(res)



def test_fun(a,b):
    print(a+b)
res=test_fun(9,4)
print(res)



"""takes nothing and returns something"""

def add():
    return 2+3
res=add()
print(res)



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def cal(f,a,b):
    return f(a,b)

ans=cal(add,3,4)
print(ans)