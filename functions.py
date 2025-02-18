def add():
    print(2+5)
    print(2+3)
add()


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



given_list=[1,2,3,4,5]
search_element=4
for ele in given_list:
    if ele==search_element:
        print("element found at idx:",idx(search_element))
    else:
        print("element not found")
    continue              