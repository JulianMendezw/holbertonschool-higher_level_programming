<div align="center"><img src="https://i.ibb.co/L9384Ks/Higher-level-programming.png"></div>

<br>
Foundations - Higher-level programming ― Python

_by Guillaume, CTO at Holberton School_


## Author’s disclaimer

```
Welcome to the Python world!

After 3 months of C, you will start Python today.
The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume, CTO at Holberton

```

## Resources

**Read or watch**:

-   [The Python tutorial](https://intranet.hbtn.io/rltoken/fX5geNeDFcCtootbB_MqCQ "The Python tutorial")  (_only the first three chapters below_)
    -   [Whetting Your Appetite](https://intranet.hbtn.io/rltoken/JnsZOCXrWDkZn6iMo1uuFg "Whetting Your Appetite")
    -   [Using the Python Interpreter](https://intranet.hbtn.io/rltoken/AejXr_G-d8CSITEtpvwpRg "Using the Python Interpreter")
    -   [An Informal Introduction to Python](https://intranet.hbtn.io/rltoken/lUBuPMNcox9EqJ1Q3oVesQ "An Informal Introduction to Python")  (_Read up until “3.1.2. Strings” included_)
-   [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/z6mk3Yep2tJVSF6KsBAYrg "How To Use String Formatters in Python 3")
-   [Learn to Program](https://intranet.hbtn.io/rltoken/gYgGXOth8N16KjUpXgO1uQ "Learn to Program")
-   [PEP 8 – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/BMIjFOY7HvWHSjHfNrkzPg "PEP 8 -- Style Guide for Python Code")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/fBqNUTa-ZywgkDpUYfAzAQ "explain to anyone"),  **without the help of Google**:

### General

-   Why Python programming is awesome
-   Who created Python
-   Who is Guido van Rossum
-   Where does the name ‘Python’ come from
-   What is the Zen of Python
-   How to use the Python interpreter
-   How to print text and variables using  `print`
-   How to use strings
-   What are indexing and slicing in Python
-   What is the official Holberton Python coding style and how to check your code with  `PEP 8`

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file at the root of the  `holbertonschool-higher_level_programming`  repo, containing a description of the repository
-   A  `README.md`  file, at the root of the folder of  _this_  project, is mandatory
-   Your code should use the  `PEP 8`  style (version  `1.7.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`

### Shell Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your scripts will be tested on Ubuntu 14.04 LTS
-   All your scripts should be exactly two lines long (`wc -l file`  should print 2)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/bin/bash`
-   All your files must be executable

### C Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be compiled on Ubuntu 14.04 LTS
-   Your programs and functions will be compiled with  `gcc 4.8.4`  using the flags  `-Wall`  `-Werror`  `-Wextra`  `and -pedantic`
-   All your files should end with a new line
-   Your code should use the  `Betty`  style. It will be checked using  [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl "betty-style.pl")  and  [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl "betty-doc.pl")
-   You are not allowed to use global variables
-   No more than 5 functions per file
-   In the following examples, the  `main.c`  files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own  `main.c`  files at compilation. Our  `main.c`  files might be different from the one shown in the examples
-   The prototypes of all your functions should be included in your header file called  `lists.h`
-   Don’t forget to push your header file
-   All your header files should be include guarded

## More Info

### Zen

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

### Install PEP8

`Pycodestyle`  is now the  [new standard of Python style code](https://intranet.hbtn.io/rltoken/D67mmHg2X9ZI7QHlQxayyw "new standard of Python style code"), but at school we will use  `PEP8`,  `version 1.7.*`  Don’t worry,  `pycodestyle`  is based on  `pep8`. The hardest part now is to install it for Python 3:

#### Regular Ubuntu 14.04 install

```
$ sudo apt-get install python3-pep8

```

#### Using Pip3

##### Install Pip3

```
$ sudo apt-get install python3-pip

```

#### Install Pep8

```
$ sudo apt-get install python3-pip
$ sudo pip3 install -Iv pep8==1.7.0

```

-> Make sure you have the right version

```
$ pep8 --version
1.7.0
$

```

Finally, if you can’t make it work, please use the “container-on-demand” tool to “PEP8” your files in a pre-configured container.
