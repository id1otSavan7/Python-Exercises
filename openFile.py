f = open(r"C:\Users\Lance\Desktop\test.txt", mode="r", encoding="utf-8")

try:
    f = open(r"C:\Users\Lance\Desktop\test.txt", mode="w", encoding="utf-8")
    f.write("Hello Lance!\n")
    f.write("Would you like to see my cat?\n")   
    f.write("You can pet it, if you want to.") 

finally:
    f = open(r"C:\Users\Lance\Desktop\test.txt", mode="r", encoding="utf-8")
    
    print(f.read())
    print(f.tell()) #Put our indicator in the end of all the characters that are in the file
    print(f.read(4)) #reads where the indicator is
    f.seek(44) #Sets our indicator
    print(f.read(4)) #reads where our indicator is
    
    f.seek(0)
    for line in f:
        print("x" + line, end="")

    f.seek(0)
    print("\n\n"+ f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    

    f.close() #Closes the fiel

