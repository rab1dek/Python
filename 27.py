# Write a Python program to concatenate all elements in a list into a string and return it

def list_to_string(list):
    str = ""
    for one in list:
        str += one
    return str

def list_to_string2(list):
    str1 = " "
    return str1.join(list)

list = ['Bula', 'Pomidor', 'Kaczka']
print(list_to_string(list))
print(list_to_string2(list))