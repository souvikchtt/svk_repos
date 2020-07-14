name=input("Enter the name: ")
age=input("Enter your age: ")
print("hello "+name+" your age is "+age)

num1=input("Enter first number: ")
num2=input("Enter second number: ")
## by default python take user input as string, if we take num1 as 3 and num2 as 4 and then use sum=num1+num2,
## we get 34 as sum result. Thus first we need to convert user input into int or float
sum=num1+num2
print("incorrect sum result is : ",sum)

sum_correct=float(num1)+float(num2)
print("Correct sum result is: ",sum_correct)