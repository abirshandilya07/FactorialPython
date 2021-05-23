print("Hello")
print("This program is made for taking out the factorial of a number")
f=input("Enter the number whose factorial you want: ")
n=int(f)
fac=1
for x in range(1,n+1):
    fac=fac*x

print("Factorial of ",n," is ",fac)    
