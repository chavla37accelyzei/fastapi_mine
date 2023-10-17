f=open("ke_file.txt",'r') 

  
#print(f.read()) 
 # presenting the what we read in the file
#print(f.readline(2)) #"h
#print(f.readlines()) # to read the lines
#print(f.readlines(1))  # perticular line onl
print(f.readline(),end = "")
print(f.readline())

# creating new file and appending data
f1=open("abc",'w')

# copying ke file data into abc file
for data in f:
    f1.write(data)

# reading image
f2 = open("tea2.jpg","rb")
img = open("tea.jpg",'wb')

for i in f2:
    print(img.write(i))



