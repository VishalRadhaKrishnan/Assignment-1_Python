Q26. What is a string? How can we declare string in Python?
    string is a sequence of characters  either enclosed within single quotes,double quotes .It is used 
represent numbers,symbols,spaces and special characters.

Q27. How can we access the string using its index?
    In python we can access the string using indexing,by this index starting character index is 0 continues
so on. we also negative indexing for reversing.

Q28. Write a code to get the desired output of the following
string = "Big Data iNeuron"
desired_output = "iNeuron"

string = "Big Data iNeuron"
print(string[8:])
output:iNeuron

Q29. Write a code to get the desired output of the following
string = "Big Data iNeuron"
desired_output = "norueNi"

string = "Big Data iNeuron"
str = (string[8:])
output = str[::-1]
print(output)
output:norueNi 

Q30. Resverse the string given in the above question.
string = "Big Data iNeuron"
output = string[::-1]
print(output)
output:norueNi ataD giB

Q31. How can you delete entire string at once?
    you cannot delete an entire string at once. Strings are immutable, which means we cannot delete the
individual characters from asyncore import loop
import operator
from unicodedata import combining
from the string.To "delete" the string, assign an empty string to the variable.
    
Q32. What is escape sequence?

Q33. How can you print the below string?
'iNeuron's Big Data Course'
print("'iNeuron's Big Data Course'")
output:'iNeuron's Big Data Course'

Q34. What is a list in Python?
    List is mutable and can store heterogenous data and we can iterarte over the elements in the list.
List contains of ordered elements and supports indexing.Represented by [ ]

Q35. How can you create a list in Python?
    There are different ways to create a list.,some of them are
        1.list1 = []
        2.my_list = list()

Q36. How can we access the elements in a list?
    we can access the elements in the list by indexing and slicing.Negative slicing also possible.

Q37. Write a code to access the word "iNeuron" from the given list.

lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
output = lst[4][2]
print(output)
output:iNeuron

Q38. Take a list as an input from the user and find the length of the list.
user_num = int(input("enter a series of number:"))
num = user_num.split()
list1 = []
print(len(list(num))
output:enter a series of number:1 2 3 4
4

Q39. Add the word "Big" in the 3rd index of the given list.
    lst = ["Welcome", "to", "Data", "course"]
    lst[2] = "Big"
    print(lst)
output:['Welcome', 'to', 'Big', 'course']

Q40. What is a tuple? How is it different from list?
    Tuple is an ordered,immutable datatype of collection of objects.It is represented by ()
    list is mutable and tuple is immutable
    list is represented by [] and tuple is represented by ()
    list can store heterogenous data and tuple also store heterogenous data 

Q41. How can you create a tuple in Python?
    we can create a tuple in some ways.,
    1.tup = ()
    2.my_tup = (1,2,3)

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer 
with reason.
    my_tuple = (1, 2, 3)
    new_tuple = my_tuple + ("vishal",)
    print(new_tuple)
output:(1, 2, 3, 'Your Name')
       ('Your Name', 1, 2, 3)
    Creating a empty tuple and adding name to that tuple is not possible. so we can create a tuple with
some values and we can add name to that tuple.

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
    tup = (1,2,3,4,5,6)
    tup1 = ("vishal","anu","priya")
    c = tup + tup1
    print(c)
output:(1, 2, 3, 4, 5, 6, 'vishal', 'anu', 'priya')

Yes we can append a tuple to other tuple and store it in other tuple. 

Q44. Take a tuple as an input and print the count of elements in it.
    tup = (1,2,3,4,5,6,7,8,9,0)
    count = len(tup)
    print(count)
output:10

Q45. What are sets in Python?
 set is an unordered collection of unique elements. Sets are defined by enclosing a comma-separated 
 sequence of elements within curly braces {} or by using the set() constructor

Q46. How can you create a set?
    You can create a set by enclosing a comma-separated sequence of elements within curly braces {}
    1.my_set = {1, 2, 3, 4, 5}
    2.you can use set() to create a set.

Q47. Create a set and add "iNeuron" in your set.
    set1 = set()
    a = set1.add("iNeuron")
    print(set1)
output:{'iNeuron'}

Q48. Try to add multiple values using add() function.
    set1 = set()
    set1.add("iNeuron")
    set1.add("vishal")
    set1.add("aravind")
    set1.add("rakshan")
    print(set1)

output:{'rakshan', 'aravind', 'iNeuron', 'vishal'}

Q49. How is update() different from add()?
    add() will add the single element to the set. for one add() we can add one element.
    Update() will update will add list of elements to set like list,tuple or another set can be added.

Q50. What is clear() in sets?
    the clear() method is used with sets to remove all elements from the set, leaving it empty. It does 
not take any arguments and does not return any value.

Q51. What is frozen set?
    A frozen set in Python is an immutable, hashable, and unordered collection of unique elements, just like a regular set.Once you create 
a frozen set, you cannot change its elements or add/remove elements from it.

Q52. How is frozen set different from set?
    Sets are mutable, which means you can add, remove, or modify elements in a set after it is created.
Frozen sets, on the other hand, are immutable. Once you create a frozen set, you cannot change its elements or add/remove elements from it. 

Q53. What is union() in sets? Explain via code.
    union() method is used to return a new set that contains all the unique elements from two or more sets.It combines the elements from 
all the sets while removing duplicates.

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_result = set1.union(set2)
    print(union_result)
    union_result = set1 | set2
Output: {1, 2, 3, 4, 5}

Q54. What is intersection() in sets? Explain via code.
    Intersection() method is used to return a new set that contains the elements that are common to two or more sets.
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    intersection_result = set1.intersection(set2)
    print(intersection_result)
Output: {3, 4}

Q55. What is dictionary in Python?
    Dictionary is a datatype of unordered collection of elements which contains data as key-value pairs.It is mutable and are represented
in {}

Q56. How is dictionary different from all other data structures.
    Dictionaries are different from other datatypes in case of Key-Value Mapping,Key-Based Access,mutable,unique,hashing,mixed data types.

Q57. How can we delare a dictionary in Python?
    we declare dictionary in many ways.,
    dict1 = dict()
    dict3 = {1:"2",2:"3",3:"4",5:"6"}
    key_value_pairs = [("name", "John"), ("age", 30), ("city", "New York")]
    my_dict = dict(key_value_pairs)
output:{}
       {1: '2', 2: '3', 3: '4', 5: '6'}    

Q58. What will the output of the following?
var = {}
print(type(var))

output:<class 'dict'>

Q59. How can we add an element in a dictionary?
    vish = dict()
    vish["name"] = ("vishal")
    vish["clg"] = ("ssn")
    vish["sis"] = ("agal","archana")
    print(vish)
output:{'name': 'vishal', 'clg': 'ssn', 'sis': ('agal', 'archana'), 'work': 'no work', 'salary': 'no salary', 'food': 'oc food'}

Q60. Create a dictionary and access all the values in that dictionary.
    vish = dict()
    vish["name"] = ("vishal")
    vish["clg"] = ("ssn")
    vish["sis"] = ("agal","archana")
    print(vish)
    print(vish["food"])
output:oc food

Q61. Create a nested dictionary and access all the element in the inner dictionary.
    student_info = {"student1": {"name": "Alice","age": 20,"grades": {"math": 95,"history": 88,"science": 92 } },
                    "student2": {"name": "Bob","age": 22,"grades": { "math": 78,"history": 92,"science": 85}}}
    student1_name = student_info["student1"]["name"]
    student2_age = student_info["student2"]["age"]

    print("Student 1 Name:", student1_name)
    print("Student 2 Age:", student2_age)
output:Student 1 Name: Alice
       Student 2 Age: 22

Q62. What is the use of get() function?
    The get() function  is a built-in method used to retrieve the value associated with a specified key in a dictionary.
Example:my_dict = {"name": "John", "age": 30}
        name = my_dict.get("name")  # Retrieves the value associated with the "name" key
        age = my_dict.get("age")    # Retrieves the value associated with the "age" key



Q63. What is the use of items() function?
    The items() function in Python is a built-in method used with dictionaries to retrieve a view of all the key-value pairs (items) 
contained within the dictionary.
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    for key,value in my_dict.items():
        print(key,value)
output:name John
       age 30
       city New York

Q64. What is the use of pop() function?
    The pop() function in Python is a built-in method used to remove an item from a dictionary based on its key and return the value 
associated with that key. It allows you to remove a specific key-value pair from the dictionary.
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    # Using pop() to remove and retrieve a specific item
    age = my_dict.pop("age")  # Removes the "age" key-value pair and returns the value (30)
output:{'name': 'John', 'city': 'New York'}

Q65. What is the use of popitems() function?
    The popitem() function  is a built-in method used to remove and return an arbitrary (key, value) pair from a dictionary.The popitem() 
method is primarily used when you want to remove and retrieve a single item from the dictionary, but you don't need to specify a 
particular key.
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    # Using popitem() to remove and retrieve an arbitrary item
    key, value = my_dict.popitem()
    print(f"Removed: Key='{key}', Value='{value}'")
    print(my_dict)
output:Removed: Key='city', Value='New York'
                {'name': 'John', 'age': 30}

Q66. What is the use of keys() function?
    The keys() function in Python is a built-in method used with dictionaries to retrieve a view object containing all the keys present 
in the dictionary.

Q67. What is the use of values() function? 
    The keys() function is a built-in method used with dictionaries to retrieve a view object containing all the keys present 
in the dictionary. 

Q68. What are loops in Python?
    In Python, loops are control structures that allow you to repeatedly execute a block of code as long as a certain condition is met or 
for a specified number of times. 

Q69. How many type of loop are there in Python?
Types of loops.,
    1.for loop
    2.while loop

Q70. What is the difference between for and while loops?
For loop -- is used when no of iterations are known and iterable values are taken by itself for each iteration.
While loop -- is used when no of iterations are unknown and we need to update the iterable value for each iteration.

Q71. What is the use of continue statement?
    Continue statement is used to skip the iteration.It is often used to filter data or perform specific processing on some elements 
of a data structure while skipping others.

Q72. What is the use of break statement?
    Break statement is used to exit a loop prematurely, regardless of whether the loop condition has been fully satisfied.
Early Termination: You can use break to exit a loop early when a specific condition is met. 
Avoiding Infinite Loops: In cases where you have a while loop, the break statement is often used as a way to exit the loop when a 
certain condition becomes true, preventing an infinite loop.

Q74. What is the use of range() function?
    The range() function in Python is used to generate a sequence of numbers within a specified range.
we can use range of function with [Start(inclusive, optional),Stop (exclusive),Step (optional)]

Q75. How can you loop over a dictionary?
We can loop over a dictionary using several methods.,
    1.Iterating Over Keys
    2.Iterating Over Values
    3.Iterating Over Key-Value Pairs

Coding problems:
Q76. Write a Python program to find the factorial of a given number.
num = int(input("enter ur number:"))
if num == 0:
    print("1") 
elif num < 0:
    print("factorial is not defined for negative numbers")
else:
    Factorial = 1
    for i in (num,num+1):
        factorial *= i
output:enter ur number:0 
1

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
principal = float(input("Enter the principal amount:"))
rate_of_interest = float(input("Enter the annual interest rate (%) : "))
time_period = float(input("Enter the time period (in years): "))
simple_interest = (principal * rate_of_interest * time_period) / 100
print(f"Simple Interest: {simple_interest}")

output:
Enter the principal amount:300000
Enter the annual interest rate (%) : 18
Enter the time period (in years): 1
Simple Interest: 54000.0


Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
principal = float(input("Enter the principal amount:"))
rate_of_interest = float(input("Enter the annual interest rate (%) : "))
time_period = float(input("Enter the time period (in years): "))
compound_interest = principal*(1 + rate_of_interest / 100)** time_period
print(f"compound_interest: {compound_interest}")

output:
Enter the principal amount:100000
Enter the annual interest rate (%) : 18
Enter the time period (in years): 1
compound_interest: 118000.0

Q79. Write a Python program to check if a number is prime or not.
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
output:
Enter a number: 2
2 is a prime number

Q80. Write a Python program to check Armstrong Number.
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        original_num = num
        sum_of_cubes = 0
        while num > 0:
            digit = num % 10
            sum_of_cubes += digit ** 3
            num //= 10

        if sum_of_cubes == original_num:
            print(f"{original_num} is an Armstrong number.")
        else:
            print(f"{original_num} is not an Armstrong number.")
output:
Enter a number: 153
153 is an Armstrong number.

Q81. Write a Python program to find the n-th Fibonacci Number.
    def fibonacci_iterative(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_values = [0, 1]
            for i in range(2, n + 1):
                next_fib = fib_values[i - 1] + fib_values[i - 2]
                fib_values.append(next_fib)
            return fib_values[n]
    n = 10
    fibonacci_number = fibonacci_iterative(n)
    print(f"The {n}-th Fibonacci number is {fibonacci_number}")
output:
The 10-th Fibonacci number is 55

Q82. Write a Python program to interchange the first and last element in a list.
    def interchange_first_last(lst):
        if len(lst) >= 2:
            lst[0], lst[-1] = lst[-1], lst[0]

    my_list = [1, 2, 3, 4, 5]
    print("Original List:", my_list)
    interchange_first_last(my_list)
    print("List after interchanging first and last elements:", my_list)
output:
Original List: [1, 2, 3, 4, 5]
List after interchanging first and last elements: [5, 2, 3, 4, 1]

Q83. Write a Python program to swap two elements in a list.
   def swap_elements(lst, idx1, idx2):
    if 0 <= idx1 < len(lst) and 0 <= idx2 < len(lst):
        temp = lst[idx1]
        lst[idx1] = lst[idx2]
        lst[idx2] = temp
        
my_list = [1, 2, 3, 4, 5]
index1, index2 = 1, 3 

print("Original List:", my_list)
swap_elements(my_list, index1, index2)
print("List after swapping:", my_list)

output:
Original List: [1, 2, 3, 4, 5]
List after swapping: [1, 4, 3, 2, 5]


Q84. Write a Python program to find N largest element from a list.
    def large_n(lst,n):
        a =  sorted(lst,reverse=True)
        return a[:n]

    lst = [12, 45, 2, 41, 31, 10, 8, 6]
    n = 3 
    largest_elements = large_n(lst, n)
    print(largest_elements)
output:
[45, 41, 31]

Q85. Write a Python program to find cumulative sum of a list.
    def sum_lst(lst):
        sum = 0
        sum_lst = []
        for i in lst:
            sum += i 
            sum_lst.append(sum)
        return sum_lst
    lst = [1,2,3,4,5,6,7]
    print(sum_lst(lst))

output : [1, 3, 6, 10, 15, 21, 28]

Q86. Write a Python program to check if a string is palindrome or not.
    str = input("enter ur string :")
    def palindrome_str(str):
        a = str[::-1]
        if a == str:
            return "palindrome"
        else:
            return "Not a palindrome"
    print(palindrome_str(str))
output:enter ur string :archana
       Not a palindrome


Q87. Write a Python program to remove i'th element from a string.

Q88. Write a Python program to check if a substring is present in a given string.
    input_string = "vishal is a smart working software engineer"
    substring = input("enter ur sustring :")
    if substring in input_string:
        print(substring," is present in the string.")
    else:
        print({substring}," is not present in the string.")
output:
enter ur sustring :smart
smart  is present in the string.

Q89. Write a Python program to find words which are greater than given length k.
    input_string = "This is a sample sentence to find words greater than a certain length."
    words = input_string.split()
    k = 5
    long_words = [word for word in words if len(word) > k]
    print("Words greater than length", k, "are:", long_words)
output:
Words greater than length 5 are: ['sample', 'sentence', 'greater', 'certain', 'length.']

Q90. Write a Python program to extract unquire dictionary values.
    input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
    unique_values = set()
    for value in input_dict.values():
        unique_values.add(value)

    unique_values_list = list(unique_values)
    print("Unique values:", unique_values_list)
output:
Unique values: [1, 2, 3]    

Q91. Write a Python program to merge two dictionary.
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    print("Merged dictionary:", merged_dict)
output:
Merged dictionary: {'a': 1, 'b': 3, 'c': 4}

Q92. Write a Python program to convert a list of tuples into dictionary.

Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

data_list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
data_dict = {}
for item in data_list:
    key, value = item
    data_dict[key] = value
print(data_dict)

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]

input_list = [9, 5, 6]
output_list = [(num, num**3) for num in input_list]
print(output_list)

Q94. Write a Python program to get all combinations of 2 tuples.
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)
combinations = []
for item1 in test_tuple1:
    for item2 in test_tuple2:
        combinations.append((item1, item2))
print(combinations)

Q95. Write a Python program to sort a list of tuples by second item.
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

input_list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
sorted_list = sorted(input_list, key=lambda x: x[1])
print(sorted_list)

Q96. Write a python program to print below pattern.
for i in range(1,6):
    for j in range(i):
        print("*",end = "")
    print()
* 
* * 
* * * 
* * * * 
* * * * * 
Q97. Write a python program to print below pattern.
num_rows = 5
for i in range(1, num_rows + 1):
    for j in range(num_rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()  

        *
      * *
    * * *
  * * * *
* * * * *
Q98. Write a python program to print below pattern.

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
Q99. Write a python program to print below pattern.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
num_rows = 5

for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
     print()
Q100. Write a python program to print below pattern.

A 
B B 
C C C 
D D D D 
E E E E E 

