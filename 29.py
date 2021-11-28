# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def check(cl1, cl2):
    print(color_list_1.difference(color_list_2))

def check2(cl1, cl2):
    color_list_diff = []
    for color in color_list_1:
        if color not in color_list_2:
            color_list_diff.append(color)
    print(color_list_diff)

check(color_list_1, color_list_2)
check2(color_list_1, color_list_2)

