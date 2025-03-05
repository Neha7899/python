a=2     #global variable
def fn():
    return a+2
print(fn())


def fn():
    b=10        #local variable
    return b-2    #using it through return
print(fn())


a=10
def fn():
    global b
    b=10
    return a+10,b+2
print(fn())
print(b)
print('hello')

print(locals())
print(globals())