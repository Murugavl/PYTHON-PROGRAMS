num1=eval(input("Enter the 1st value: "))
num2=eval(input("Enter the 2nd value: "))
def add(num1,num2):
  print("\n\tThe Addition of",num1,"and",num2,"is       ",(num1+num2))
def sub(num1,num2):
  print("\tThe Subtraction of",num1,"and",num2,"is    ",(num1-num2))
def mul(num1,num2):
  print("\tThe MUltiplicaiton of",num1,"and",num2,"is ",(num1*num2))
def div(num1,num2):
  print("\tThe Division of",num1,"and",num2,"is       ",(num1/num2))
def rem(num1,num2):
  print("\tThe Remainder of",num1,"and",num2,"is      ",(num1%num2))
print("\n\t\tARTIHMETIC OPERATIONS")
print("\t\t ---------------------")
add(num1,num2)
sub(num1,num2)
mul(num1,num2)
div(num1,num2)
rem(num1,num2)