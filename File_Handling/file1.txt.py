#opening a file ,then write it and lastly close it.
f=open("file2.txt","w")
f.write("woops! I have deleted the content.It is me.I am guilty for that.How are u?.....")
f.close()

#open and read the file after writing
f=open("file2.txt","r")
print(f.read())
