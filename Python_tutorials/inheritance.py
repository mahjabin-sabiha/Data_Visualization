class person:
 def __init__(self,fname,lname):
  self.firstname=fname
  self.lastname=lname
 def printname(self):
  print(self.firstname,self.lastname)
class student (person):
  pass
x=student("Mike","Olsen")
x.printname()
