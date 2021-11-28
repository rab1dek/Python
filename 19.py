# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

import re
def is_check(txt):
    str = re.split(r'\s', txt)
    if str[0] == "Is":
        return txt
    else:
        return "Is " + txt

txt = "Siema jestem Tomek"
txt2 = "Is he buła?"
print(is_check(txt))
print(is_check(txt2))