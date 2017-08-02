a=int(input("Enter a number"))
f=1
if a < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif a == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,a + 1):
       f = f*i
   print("The factorial of",a,"is",f)
