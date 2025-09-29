import os

current_directory = os.getcwd()

result = os.listdir(current_directory)
#os.mkdir("test")
#os.rename("test.txt", "letter.txt")
os.remove("letter.txt")
print(result)