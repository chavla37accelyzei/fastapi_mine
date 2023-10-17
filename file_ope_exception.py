import os
# file operations
#strip() removes given char from both ends
f= open("file2.txt",'r')
line = f.readline()
print("before strip:",line)

line2=line.strip("A")
print("after strip:",line2)

line3=line.strip(" ")
print("after strip only spaces:",line3)


# right strip
line4 = line.rstrip("e")
print("removeing right char:",line4)







    

