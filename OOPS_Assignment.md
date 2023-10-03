Q1. What is the purpose of Python's OOP?
*** The purpose of Object-Oriented Programming (OOP) in Python, as in any other programming language, is to facilitate the organization, structuring, and management of code
Here are some key purposes of OOP in Python:
    ==>Abstraction
    ==>Encapsulation
    ==>Modularity
    ==>Modularity
    ==>Polymorphism
    ==> Code Reusability
    
Q2. Where does an inheritance search look for an attribute?
*** In Python, when you access an attribute (a variable or a method) on an object, the interpreter performs an inheritance search to determine where to find that attribute. This search follows a specific order known as the Method Resolution Order (MRO)
===> Instance Attributes: Python first checks if the attribute exists in the instance itself. If the attribute is found in the instance, it is used, and the search stops.

===> Class Attributes: If the attribute is not found in the instance, Python checks the class of the instance. If the attribute is found in the class, it is used.

===> Base Classes (Superclasses): If the attribute is not found in the instance or the class, Python proceeds to check the base classes (superclasses) of the class in a specific order. 

===> Object Class: If the attribute is not found in the instance, class, or any base classes, Python ultimately checks the built-in object class, which is the base class for all classes in Python. If the attribute is not found here, Python raises an AttributeError.

Q3. How do you distinguish between a class object and an instance object?
Class Object:
    A class object is a blueprint for creating instances. It defines the structure and behavior of objects that belong to that class.
    Class objects are created using the class keyword in Python.
    They typically contain class-level attributes (variables) and methods (functions) that are shared among all instances of the class.
    Class objects are usually used to create instances by calling the class as a constructor function.
Instance Object:
    An instance object is a specific object created from a class. It represents a concrete realization of the class blueprint.
    Instances are created by calling the class as a constructor function. Each instance has its own set of instance attributes and can have its own state and behavior.
    Instances are distinct and independent objects that can have different values for their attributes

Q4. What makes the first argument in a class’s method function special?
    *** In Python, the first argument in a class's method function is conventionally named self, although you can technically name it whatever you like (though it's highly recommended to stick with self for readability and convention).

    *** Instance Reference: self is a reference to the instance of the class on which the method is called. It allows you to access and manipulate the attributes and methods specific to that instance.

Q5. What is the purpose of the init method?
    The __init__ method in Python is a special method (also known as a constructor) that serves the purpose of initializing the attributes and state of an object when it is created from a class. It is one of the fundamental methods in a class and is automatically called when you create a new instance of that class.
    *** Initialization of Attributes
    *** Parameter Passing
    *** Instance Configuration
    *** Initialization Logic

Q6. What is the process for creating a class instance?
    To create an instance of a class in Python, you need to follow a specific process. Here are the steps for creating a class instance
    Define the Class: First, you need to define a class using the class keyword. The class serves as a blueprint for creating instances.
    Instantiate the Class: To create an instance of the class, you call the class as if it were a function, passing any required arguments to the __init__ method. This process is known as instantiation.
    Access Instance Attributes and Methods: You can access the attributes and methods of the instance using dot notation (instance_name.attribute_name or instance_name.method_name()).

Q7. What is the process for creating a class?
    Creating a class in Python involves defining a blueprint for creating objects (instances) with shared attributes and methods. Here's the process for creating a class.,
====> Use the class Keyword: To start defining a class, use the class keyword, followed by the name of the class. Class names are typically written in CamelCase (capitalizing the first letter of each word). 

====> Define Class Attributes: Class attributes are variables that are shared by all instances of the class. They are defined within the class but outside of any methods. Class attributes are usually constants or shared data.

===> Define the __init__ Method: The __init__ method is a special method called a constructor. It initializes the instance-specific attributes of objects when they are created. 

Q8. How would you define the superclasses of a class?
    In Python, you can define the superclasses (also known as base classes or parent classes) of a class by specifying them in the class definition using parentheses after the class name. Superclasses are the classes from which a class inherits attributes and methods. This is known as class inheritance
    
Q9. What is the relationship between classes and modules?
Classes: 
    Classes are used to define blueprints for creating objects (instances). They encapsulate data (attributes) and behavior (methods) related to a specific entity or concept. Classes are a core component of object-oriented programming (OOP) and are used for modeling real-world objects and their interactions.
Modules: 
    Modules are used to organize Python code into separate files or units. They can contain variables, functions, and classes. Modules are a way to manage and structure code for better code reuse and maintainability. Modules can be imported into other Python scripts or modules to access their contents.

Q10. How do you make instances and classes?
Define a Class:
    *** Start by defining a class using the class keyword.
    *** Inside the class definition, you can specify attributes (variables) and methods (functions) that define the behavior of instances created from the class.
Instantiate a Class:
    *** To create instances of a class, you call the class as if it were a function, passing any required arguments to the __init__ method (the constructor).
    *** The __init__ method initializes the instance attributes based on the arguments you provide.
Access Instance Attributes and Methods:
    *** You can access the attributes and methods of instances using dot notation (instance.attribute or instance.method()).
    *** This allows you to work with the data and behavior defined within the class for each instance.

Q11. Where and how should be class attributes created?
Define Class Attributes in the Class Scope:
   *** Class attributes should be defined directly within the class, at the top level, outside of any class methods. You can define them after the class name and before any methods.

Accessing Class Attributes:
   *** You can access class attributes using either the class name or an instance of the class

Updating Class Attributes:
    *** Class attributes can be modified using the class name. However, when you modify a class attribute through an instance, it creates a new instance attribute with the same name, which shadows the class attribute within that instance:

Q12. Where and how are instance attributes created?
    Instance attributes in Python are created within the __init__ method of a class. The __init__ method is a special method known as a constructor, and it is called when you create a new instance of a class. Inside the __init__ method, you can initialize instance-specific attributes (variables) by assigning values to them using the self keyword.
Define the __init__ Method:
    In your class definition, include the __init__ method with self as its first parameter. The self parameter represents the instance being created and is used to refer to instance attributes within the method.

Q13. What does the term "self" in a Python class mean?
    In Python, the term "self" is a convention used to refer to the instance of a class within that class's methods. It is the first parameter of most instance methods and is used to access and manipulate instance attributes and methods. While "self" is a convention, you can technically use any name for this parameter, but it is highly recommended to stick with "self" for clarity and convention.
*** Represents the Instance
***Accesses Instance Attributes
***Calls Instance Methods
***Implicitly Passed

Q14. How does a Python class handle operator overloading?
    In Python, operator overloading allows you to define the behavior of standard operators (such as +, -, *, /, ==, !=, etc.) for objects of a custom class. This means you can make instances of your class behave like built-in types when using operators on them. Operator overloading is achieved by defining special methods in your class, which are also known as magic methods or dunder methods (due to their double underscores).
*** Arithmetic Opertors
*** Comparison Operators
*** Other Operators

Q15. When do you consider allowing operator overloading of your classes?
    Operator overloading for your classes in Python can be considered in various situations, depending on the needs of your program and the objects you are modeling. Here are some scenarios when allowing operator overloading for your classes can be beneficial.

Q16. What is the most popular form of operator overloading?
    In Python, operator overloading allows you to define the behavior of standard operators (such as +, -, *, /, ==, !=, etc.) for objects of a custom class. This means you can make instances of your class behave like built-in types when using operators on them. Operator overloading is achieved by defining special methods in your class, which are also known as magic methods or dunder methods (due to their double underscores).
*** Arithmetic Opertors
*** Comparison Operators
*** Other Operators

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Classes and Objects:
Classes: 
    A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that objects created from the class will have. Classes encapsulate the behavior and state of objects. Understanding how to define and use classes is crucial in OOP.
Objects (Instances): 
    Objects are instances created from a class. They represent individual entities with their own unique state. Objects can access the attributes and methods defined in their class. Understanding how to create, manipulate, and interact with objects is essential in OOP.
Inheritance and Polymorphism:
Inheritance: 
    Inheritance is a fundamental concept in OOP that allows you to create new classes (child classes or subclasses) based on existing classes (parent classes or superclasses). Child classes inherit attributes and methods from their parent classes, promoting code reuse and hierarchy.
Polymorphism:
     Polymorphism is the ability of different objects to respond to the same method or function call in a way that is appropriate for their individual types. It allows you to write code that can work with objects of different classes in a consistent manner.

Q18. Describe three applications for exception processing.
Error Handling:
    Exception processing is primarily used for error handling. It allows you to gracefully handle errors that might occur during the execution of your code, preventing your program from crashing or producing incorrect results.
Resource Management:
    Exception processing is used to manage resources like files, network connections, and database connections. When using such resources, it's crucial to ensure they are properly opened, used, and closed, even in the presence of exceptions.
Control Flow and Program Logic:
    Exception processing can also be used for controlling program flow and logic in certain situations. It allows you to handle specific exceptional conditions in a way that deviates from the normal program flow.

Q19. What happens if you don't do something extra to treat an exception?
    If we don't do something extra to treat an exception in your Python code, the exception will propagate up the call stack until it is either handled by an exception handler or, if no appropriate handler is found, it will result in your program terminating abruptly. This behavior is known as an unhandled exception.

Q20. What are your options for recovering from an exception in your script?
    When an exception occurs in your Python script, you have several options for recovering from it or gracefully handling the exceptional situation. The appropriate approach depends on the nature of the exception and your program's requirements. Here are some common options for recovering from exceptions:
*** Using try-except Blocks
*** Logging Errors
*** Custom Error Handling
*** Retry Mechanisms
*** Fallback Values or Default Behavior

Q21. Describe two methods for triggering exceptions in your script.
    In Python, you can trigger exceptions deliberately in your script using various methods. Triggering exceptions is useful for testing error-handling code or handling exceptional cases in your application.
*** Raise Statement
*** Assertion Error

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of
whether or not an exception exists.
    In Python, you can specify actions to be executed at termination time, regardless of whether or not an exception occurs, by using two primary methods:
*** finally Blocks
*** Context Managers (with Statements)

Q23. What is the purpose of the try statement?
    The try statement in Python serves the purpose of defining a block of code where you expect exceptions to occur. It allows you to handle exceptions gracefully and take specific actions in response to those exceptions.
*** Exception Handling
*** Error Recovery
*** Resource Management
*** Clean Code Execution

Q24. What are the two most popular try statement variations?
Basic try-except:
    This is the most commonly used form of the try statement. It allows you to catch and handle exceptions of a specific type within a try block and provide custom error-handling code in the associated except block.
try-except-else:
    This variation extends the basic try-except form by including an else block. The else block is executed if no exception occurs within the try block.

Q25. What is the purpose of the raise statement?
    The raise statement in Python is used to explicitly raise an exception or error within your code. Its primary purpose is to signal that an exceptional situation has occurred and to trigger the execution of an associated exception handler.
*** Exception Triggering
*** Custom Exceptions
*** Error Signaling
*** Exception Propagation
*** Error Handling

Q26. What does the assert statement do, and what other statement is it like?
    The assert statement in Python is used to test whether a given expression or condition is True. If the expression evaluates to False, the assert statement raises an AssertionError exception with an optional error message. Its primary purpose is to perform debugging checks in your code, helping you identify and fix issues early during development.

Q27. What is the purpose of the with/as argument, and what other statement is it like?
    The with statement in Python is used in conjunction with a context manager to simplify resource management, such as opening and closing files, database connections, or network sockets. The with/as argument in the with statement serves the purpose of assigning a name (often referred to as a context variable) to the result of the context manager's __enter__ method. This context variable can then be used within the with block.
*** Resource Management
*** Cleaner Code
*** Scoped Variables

Q28. What are *args, **kwargs?
    In Python, *args and **kwargs are special syntax used in function definitions to pass a variable number of arguments to a function. They allow you to work with a flexible number of positional arguments (*args) and keyword arguments (kwargs) without needing to specify them explicitly when defining the function
*args (Arbitrary Positional Arguments):
    The *args syntax allows a function to accept a variable number of positional arguments. The term "args" is just a convention; you can use any valid variable name preceded by an asterisk.
**kwargs (Arbitrary Keyword Arguments):
    The **kwargs syntax allows a function to accept a variable number of keyword arguments (key-value pairs). Similar to *args, "kwargs" is a naming convention, and you can use any valid variable name preceded by double asterisks.

Q29. How can I pass optional or keyword parameters from one function to another?
    To pass optional or keyword parameters from one function to another in Python, you can use a combination of *args and **kwargs along with the * and ** unpacking operators. This approach allows you to pass a variable number of positional and keyword arguments from the calling function to the called function
*** Passing Optional or Positional Arguments (*args)
*** Passing Keyword Arguments (kwargs)

Q30. What are Lambda Functions?
    Lambda functions in Python, often referred to as "anonymous functions" or "lambda expressions," are small, inline, and anonymous functions that are defined using the lambda keyword. Lambda functions are typically used for simple operations that can be expressed in a single line of code  

Q31. Explain Inheritance in Python with an example?
    Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class (called a subclass or derived class) by inheriting properties and methods from an existing class (called a superclass or base class). In Python, you can implement inheritance using the class keyword, and it enables you to build hierarchical and reusable code structures.

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?
    In Python, when a class inherits from multiple parent classes (multiple inheritance), the method resolution order (MRO) determines which version of a method gets invoked when called from an object of the derived class.

Q33. Which methods/functions do we use to determine the type of instance and inheritance?
isinstance() function:
    The isinstance() function is used to check if an object is an instance of a particular class or a tuple of classes. It returns True if the object is an instance of at least one of the specified classes; otherwise, it returns False.
type() function:
    The type() function is used to get the type of an object. It returns the class or type of the object.
issubclass() function:
    The issubclass() function checks if a class is a subclass of a specified class or a tuple of classes. It returns True if the class is a subclass of at least one of the specified classes; otherwise, it returns False.
super() function:
    The super() function is used to access methods and properties of a superclass from a subclass. It's often used when you want to override a method in a subclass but still need to call the overridden method from the superclass.

Q34.Explain the use of the 'nonlocal' keyword in Python.
In Python, the nonlocal keyword is used to indicate that a variable in a nested function should refer to a variable in the nearest enclosing (non-global) scope that is not global. It allows you to assign values to variables in an outer (but non-global) scope, effectively bridging the gap between the local scope of the nested function and the enclosing scope.

The primary use cases for the nonlocal keyword are:
Nested Functions:
    When you have a nested function (a function defined inside another function), and you want to modify a variable from the outer function's scope within the inner function, you can use nonlocal to indicate that the variable is not local to the inner function.
Closures:
    nonlocal is often used in closures, which are functions that "remember" and can access variables from their containing (enclosing) scope even after the outer function has finished executing.

Q35. What is the global keyword?
    In Python, the global keyword is used to indicate that a variable declared within a function should refer to a global variable with the same name, rather than creating a new local variable within the function's scope.