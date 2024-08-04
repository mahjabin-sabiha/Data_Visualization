def tri_recursion(k):
 if(k>0):
	 retult=k+tri_recursion(k-1)
	 print(result)
 else:
	 result=0
 return result
print("\nRecursion examples Results")
tri_recursion(6)
