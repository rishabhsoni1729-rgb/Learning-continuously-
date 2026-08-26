# this function will , help you to take input from user and cool part is you can make calculator thru it.

a = input("Enter a is :")
b = input("Enter b is :")

print("Number a is : ", a )
print("Number b is: ", b)
print("Sum is", a+b)

# if a=3, b=2 then a+b =32 not 5 they will get concatinate. 
#but why it happens , because here a and b will take values at string not int 

# so now if you want to add then you have to put like ,shown below :
a = int(input("Enter a is :"))     #for multiple cursor holt Alt for long time
b = int(input("Enter b is :"))

print("Number a is : ", a )
print("Number b is: ", b)
print("Sum is", a+b)