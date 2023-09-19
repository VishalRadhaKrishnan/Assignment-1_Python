## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
    Python is a versatile language that can be used to develop wide variety of software applications. Its a highlevel programming language because it provides a high level of abstraction and it has rich standard library.python provides readability and simplicity in its python syntax.

Q2. Why is Python called a dynamically typed language?
    Python is a dynamically typed language because variable types are determined and checked at runtime, rather than being explictly declared or checked at compile time.

Q3. List some pros and cons of Python programming language?
    Pros : Readability and Clean Syntax           Cons : Slower Execution Speed
           Large Standard Library                        Not Ideal for Mobile or Game Development
           Dynamic Typing                                Limited Support for Mobile Platforms
           High-Level Abstractions                       Design Restrictions

Q4. In what all domains can we use Python?
    Web development
    Data science and machine learning
    Artificial Intelligence
    Scientific computing

Q5. What are variable and how can we declare them?
        Variable is an memory location in a computer that we can store values or data.Variables declared by by a name contains alphabet in start and can use underscore in symbol.

Q6. How can we take an input from the user in Python?
    we can get input from user by declaring a empty variable and declaring in what data type the user wants enter the value or data.

Q7. What is the default datatype of the value that has been taken as an input using input() function?
    Input function gets the string (str) data type .

Q8. What is type casting?
    Type casting is changing the data type of a value or expression to another data type to apply operations on it.

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
    No we can't take more input using single input function. If we multiple inputs we should use it each time for an input.

Q10. What are keywords?
    Keywords, also known as reserved words, are special words in a programming language that have predefined meanings and cannot be used for other purposes

Q11. Can we use keywords as a variable? Support your answer with reason.
    We cannot use keyword as a variable because it has predefined meanings.

Q12. What is indentation? What's the use of indentaion in Python?
    Indentation can be used to represent nested code blocks. When code blocks are nested inside one another, they are indented further to the right.

Q13. How can we throw some output in Python?
    we can get the output by using the print function.what we are calling in print function it will be throw as an output.

Q14. What are operators in Python?

Q15. What is difference between / and // operators?
    single slash will give you the output with the float value
    Double slash will give you the round value as integer datatype.

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron

x = 'iNeuron'
y = x*4
print(y)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
num = int(input("enter ur number:"))
if (num % 2 == 0):
    print("even number")
else:
    print("odd number")

Q18. What are boolean operator?
    Boolean operators are True or False value

Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```

Q20. What are conditional statements in Python?
    Conditional statements are if,elif,else 

Q21. What is use of 'if', 'elif' and 'else' keywords?
    if - it will be executed first in the program
    elif - if the if condition is not satisfied elif condition will be printed
    else - if both if and elif statements are not satisfied else statements will be printed

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age = int(input("enter ur age:"))
if age >= 18:
    print("I can vote")
else:
    print("You cannot vote")

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]

sum_of_evens = 0


for number in numbers:
    if number % 2 == 0:
        sum_of_evens += number
print("Sum of even numbers:", sum_of_evens)


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
print("The greatest number is:",round (greatest))

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number % 5 == 0:
        if number > 150:
            continue
        elif number > 500:
            break
        else:
            print(number)
