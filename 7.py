# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

filename = input("Write a filename: ")
list = filename.split(".")
print(list[-1])