# Assignment1
# section1
# print(),input(),Variables and naming rules


# Q1.write a program to display your name,college name,and favourite programming language using print()

# student={
#     "name":"Tanishka"
#     "college_name":"Zealpolytechnic"
#     "Fav_programming_language":"python"
# }
# print(student)

# Q2. Take a user input for name and age,then display:"Hello jango,you are 9 years old."

# name=(input("Enter your name:"))
# age=int(input("enter your age:"))

# print("hello",name)
# print("Your age is",age)

# Q3.Create variables for: student name, roll number,percentage, passed status.
# print all values in a formatted way

# class Student:
#     student_name = "Tanishka"
#     roll_number = 101
#     percentage = 85.5
#     passed_status = True
    
#     print("Student Name:", student_name)
#     print("Roll Number:", roll_number)
#     print("Percentage:", percentage, "%")
#     print("Passed Status:", passed_status)
        
# Q4.
# Identify which of the following variable names are invalid and rewrite them correctly:
# ● 1name
# ● student-name
# ● class
# ● total marks
# ● user_name       

# name1 = "Tanishka"
# student_name = "Tanishka"
# class_name = "AIML"
# total_marks = 80
# user_name = "tanishka9993"


#Section2 
# Data Types and Type conversion

#Q5.Create variables of type:
# ● float
# ● int
# ● str
# ● bool
# Print each variable with its data type using type()

# float_var = 80.85
# int_var = 121
# str_var ="Tanishka"
# bool_var = "True"

# print(float_var,type(float_var))
# print(int_var,type(int_var))
# print(str_var,type(str_var))
# print(bool_var,type(bool_var))

#Q6. Take 2 numbers as input from the user and display their sum
 
# num1=int(input("Enter 1st number:"))
# num2=int(input("Enter 2nd number:"))

# sum=num1+num2
# print("sum=",sum)

#Q7.Take a decimal number as input and convert it into:
# ● integer
# ● string
# Display all converted values

# decimal_num= float(input("Enter a decimal number:"))

# integer_num= int(decimal_num)
# string_num= str(decimal_num)

# print("Original decimal number:",decimal_num)
# print("Converted to integer:",integer_num)
# print("Converted to string:",string_num)

#Q8.Take user input for age and check whether the input type is string or integer.

# age= input("Enter your age:")
# print("Value Entered:",age)
# print("Data Type:",type(age))

#Section3:Operators

#Q9.Write a program to perform:

# ● Addition
# ● Subtraction
# ● Multiplication
# ● Division
# ● Modulus
# on two user-input numbers
# num1=int(input("Enter 1st no:"))
# num2=int(input("Enter 2nd no:"))

# print("Addition=",num1+num2)
# print("Subtraction=",num1-num2)
# print("Multiplication=",num1*num2)
# print("Division=",num1/num2)
# print("Modulus=",num1%num2)

#Q10.Take two numbers and display:

# Take two numbers and display:
# ● Greater than
# ● Less than
# ● Equal to
# ● Not equal to
# comparison results.

# num1=int(input("Enter 1st no:"))
# num2=int(input("Enter 2nd no:"))

# print("Greater than:",num1>num2)
# print("Less than:",num1<num2)
# print("Equal to:",num1==num2)
# print("Not equal to:",num1!=num2)

#Q11.Create a login system using logical operators
#Username must be"admin"
#password must be"12345"
#Display login successfull or failure

# print("Login by using username and password")
# username = input("Enter username:")
# password = input("Enter password:")

# if username=="admin" and password=="12345":
#     print("Login Successfull!!!")
# else:
#     print("Login Failure!!")

#Q12.Write a program to check whether a number is:
# ● Positive
# ● Negative
# ● Zero

# num= int(input("Enter a number:"))

# if num<0:
#     print("The number is negative")
# elif num>0:
#     print("The number is positive")
# else :
#     print("zero")

#Section 4: Conditional Statements (if / elif / else)
#Q13.Take marks as input and print grade:
# ● A → 90 and above
# ● B → 75 to 89
# ● C → 50 to 74
# ● Fail → below 50

# marks=float(input("Enter your marks:"))
# if marks>90:
#     print("A Grade")
# elif marks>75:
#     print("B Grade")
# elif marks>50:
#     print("C Grade")
# else:
#     print("Fail!!!")

#Q14.Write a program to check whether number is even or odd

# num=int(input("Enter a number:"))

# if num%2==0:
#     print("The number is even")
# else:
#     print("number is odd")

#Q15.Take age as input and determine:
# ● Child
# ● Teenager
# ● Adult
# ● Senior Citizen

# age=int(input("Enter the age:"))
# if age<=10:
#      print("Child")
# elif age<=20:
#      print("Teenager")
# elif age<=40:
#      print("Adult")
# else:
#      print("Senior Citizen")

#Q17.Print numbers from 1 to 20 using a for loop.

# for i in range(1,21):
#     if i==5:
#         continue
#     print(i)

#Q18. Print all even numbers between 1 and 50

# nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# even=[]
# for x in nums:
#     if x %2==0:
#         even.append(x)
# print("Even numbers.",even)

#Section 6:
# Breaks and continue

#Q23.Print numbers from 1 to 20, but stop the loop when the number becomes 15.

# for i in range(1,20):
#       if i==15:
#           break
#       print(i)

#Q24.Print numbers from 1 to 20, skipping all multiples of 3.







