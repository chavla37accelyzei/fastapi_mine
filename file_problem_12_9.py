import os
file = input("enter a file with extension")
file_name,file_extension = os.path.splitext(file)
print("file name:",file_name)
print("file extension",file_extension)

#check about .mp3 extension files
if file_extension == ".mp3":
    print("mp3 files are not allowed")

else:
    print("this file is allowed")

# or
# if file.endswith(".mp3"):
     #print(" mp3 files not allowed")
    
 # else:print("alow this file")

 


