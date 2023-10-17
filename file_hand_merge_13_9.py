# open a file
# read file
import os
f1 = open("demo.txt","w")
f1.write("documentation should be clean and simple")
f1.close()  # close the file after your work

print("reading data")
f1 = open("demo.txt","r")
my_data = f1.read()   # store read data in variable
print("demo file data:",my_data)
f1.close()

# 
print("appending data")
f1 = open("demo.txt","a")
f1.write("you learn new things every day")
f1.close()


print(" data appended & file closed")

#f1.append("you learn everyday")

# delete files
print("delete files fileobj.remove(file_name)")
os.remove("file2.txt") 

# to avoid error first check whether the file exist or not
if os.path.exists("none.txt"):
    os.remove("none.txt")
else:
    print("such a file not exist in your system")

print("we can remove dir --> os.rmdir(folder)") # can remove empty folders only




