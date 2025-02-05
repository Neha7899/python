"""dictionary datatype"""

"""type of the data"""
a={"course":"python"}
print(type(a))


"""accessing the value using key in dict datatype"""

a={"course":"AIML"}
print(a["course"])


"""printing a dictionary variable"""

a={"name":["neha","sweety","minnu"],"gender":"female","e-mail":["ababbgmail.com","bababgmail.com"]}
print(a)
print(a["name"])
print(a["gender"])
print(a["e-mail"])



"""appending to a dictionary"""

a={"name":["neha","sweety","minnu"]}
a["name"].append("srishanth")
print(a)



"""updating the dictionary's value in a key"""


a={"name":["neha"]}
print(a)
a["name"][0]="sweety"
print(a)


a={"name":["neha","reddy","a"]}
a["name"][2]="addula"
print(a)