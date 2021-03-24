def add(num1,num2):
  print("your sum of numbers:",num1+num2)
def sub(num1,num2):
    print("your result :",num1-num2)
def mul(num1,num2):
    print("your result :",num1*num2)
def  div(num1,num2):
    print("your result :",num1/num2)

first_number=int(input("please give me your firstnumber"))
second_number=int(input("Please provide your second number"))
operation=input("please select your option +_*/")

if operation=="+":
    add(first_number,second_number)
elif operation=="-":
    sub(first_number,second_number)
elif operation=='*':
    mul(first_number,second_number)
elif operation=="/":
    div(first_number,second_number)
else:
    print("Please select valid operation")

