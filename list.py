""" accessing the elements from a list through positive indexing
it prints the elements from start """
a=[15,24,12,98,"True"]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])


""""accessing the elements from the list through negative indexing
it prints the elements from reverse or last"""
a=[15,24,12,98,"True"]
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])


"""len is a keyword which is used to know the length of a list or how many elements are there in a list"""
a=[23,45,27,45,63]
print(len(a))    



"""list slicing"""
a=[1,2,3,4,5]
print(a[0:2]) #starting index-0,ending index=2 but not included
print(a[3:])   #it takes ending index of the last element of the list defaultly
print(a[:3])   #it takes starting index of the list as 0 defaultly
print(a[-3:-1])
    
"""accessing elements present in even and odd positions"""
a=[2,3,4,5,6,7]
print(a[::2])     #with step size of 2,we can access the elements present in even position
print(a[1::2])     #with the 1 as start index and 2 as step size, we can access the elements present in odd positions



""""reversing a list"""
a=[10,20,30,40,50]
print(a[::-1])
