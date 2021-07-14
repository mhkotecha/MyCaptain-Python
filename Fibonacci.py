# Program to display the Fibonacci sequence up to n-th term

nthterm = int(input("How many terms do you want? "))

# declare the first two terms to initiate sequence
n1 = 0
n2 = 1
count = 0

# check if the number entered by user is valid
if nthterm <= 0:
   print("Please enter a positive integer")
   
# if user wants only 1st term, then print n1
elif nthterm == 1:
   print("Fibonacci sequence upto", nthterm ,":")
   print(n1)

# generate sequence
else:
   print("Fibonacci sequence:")
   while count < nthterm:
       print(n1)
       nth = n1 + n2
       # change values so that the previous 2 terms remain as n1 and n2 
       n1 = n2
       n2 = nth
       count = count + 1

