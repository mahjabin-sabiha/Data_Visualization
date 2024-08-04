#Deleting a file
import os
if os.path.exists("demofile.txt"):
	os.remove("demofile.txt")
else:
	print("This file does not exist")
