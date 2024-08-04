#opening a file then appened it and lastly closed it......... 

f=open("file.txt","a")
f.write("Now the file has more content!")
f.close()

#open and read the file after appending
f=open("file.txt","r")
print(f.read())
 
