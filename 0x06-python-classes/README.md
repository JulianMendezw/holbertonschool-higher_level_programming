# 0x06. Python - Classes and Objects

Foundations - Higher-level programming ― Python

_by Guillaume, CTO at Holberton School_

## Background Context

OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow. As usual, make sure you type (never copy and paste), test, and understand all examples shown in the following links (including those in the video). The biggest and most important task of this project is the reading. The project itself will not take you more than 2-3 hours if you take the time to read and understand everything.

Read or watch the below resources in the order presented.

## Resources

**Read or watch**:

-   [Object Oriented Programming](https://intranet.hbtn.io/rltoken/izl1kO1isRJo6h_Ce2pmhw "Object Oriented Programming")  (_Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes,  `classmethod`  and  `staticmethod`  yet_)
-   [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/K5t1QFchQYs7rkt62uMo7A "Object-Oriented Programming")  (_Please *_be careful*_: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The  `__init__`  Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”_)
-   [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/LZg7XYGGZj49Gu2276afpA "Properties vs. Getters and Setters")
-   [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/aFk7Ki8TPw5vZZBx2JXvIQ "Learn to Program 9 : Object Oriented Programming")
-   [Python Classes and Objects](https://intranet.hbtn.io/rltoken/CFTUXsxbTVu4xb698_2bmQ "Python Classes and Objects")
-   [Object Oriented Programming](https://intranet.hbtn.io/rltoken/DK1vkIQ0xT1fmMrmBcSGiA "Object Oriented Programming")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/aul-KtyIrNZ8J5M_Pjxyjg "explain to anyone"),  **without the help of Google**:

### General

-   Why Python programming is awesome
-   What is OOP
-   “first-class everything”
-   What is a class
-   What is an object and an instance
-   What is the difference between a class and an object or instance
-   What is an attribute
-   What are and how to use public, protected and private attributes
-   What is  `self`
-   What is a method
-   What is the special  `__init__`  method and how to use it
-   What is Data Abstraction, Data Encapsulation, and Information Hiding
-   What is a property
-   What is the difference between an attribute and a property in Python
-   What is the Pythonic way to write getters and setters in Python
-   How to dynamically create arbitrary new attributes for existing instances of a class
-   How to bind attributes to object and classes
-   What is the  `__dict__`  of a class and/or instance of a class and what does it contain
-   How does Python find the attributes of an object or class
-   How to use the  `getattr`  function

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (version 1.7)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## More Info

**Documentation is now mandatory!**  Each module, class, and method must contain docstring as comments.  [Example Google Style Python Docstrings](https://intranet.hbtn.io/rltoken/SYdQnrcR2jL5hIs5TkIN5Q "Example Google Style Python Docstrings")