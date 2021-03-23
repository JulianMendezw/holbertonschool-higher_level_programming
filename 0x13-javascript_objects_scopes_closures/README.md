# 0x13. JavaScript - Objects, Scopes and Closures

-   Foundations - Higher-level programming ― JavaScript
-   By Guillaume, CTO at Holberton School


## Resources

**Read or watch**:

-   [JavaScript object basics](https://intranet.hbtn.io/rltoken/OJ4pU6uHwfCrAclbZsk_Hg "JavaScript object basics")
-   [Object-oriented JavaScript](https://intranet.hbtn.io/rltoken/Uqv-UMsBUpHWQZXBf5fn0g "Object-oriented JavaScript")  (_**read all examples!**_)
-   [Class - ES6](https://intranet.hbtn.io/rltoken/zMWxOmGWEsOCldCKeDswCA "Class - ES6")
-   [super - ES6](https://intranet.hbtn.io/rltoken/DTMKogwFYEgUnpLrNvTcfQ "super - ES6")
-   [extends - ES6](https://intranet.hbtn.io/rltoken/fh2JHfNNa-HLnmfSdOo9TA "extends - ES6")
-   [Object prototypes](https://intranet.hbtn.io/rltoken/lrlwnQMM82RimJJcfLao5w "Object prototypes")
-   [Inheritance in JavaScript](https://intranet.hbtn.io/rltoken/LDpXxzBrdmmXAHoNrWwLxg "Inheritance in JavaScript")
-   [Closures](https://intranet.hbtn.io/rltoken/qDa7F8060Jlhe3DZZitY4A "Closures")
-   [this/self](https://intranet.hbtn.io/rltoken/ockP7FQKKmTRvfeAHw-XSw "this/self")
-   [Modern JS](https://intranet.hbtn.io/rltoken/22mdHf9KeFhRQrLP-e1hPw "Modern JS")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/JeG-kC426HCi3zYomikQvw "explain to anyone"),  **without the help of Google**:

### General

-   Why JavaScript programming is amazing
-   How to create an object in JavaScript
-   What  `this`  means
-   What  `undefined`  means
-   Why the variable type and scope is important
-   What is a closure
-   What is a prototype
-   How to inherit an object from another

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS using  `node`  (version 10.14.x)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/node`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be  `semistandard`  compliant.  [Rules of Standard](https://intranet.hbtn.io/rltoken/LzTXpt_3kwzaaEQFTvq2UQ "Rules of Standard")  +  [semicolons on top](https://intranet.hbtn.io/rltoken/_6jQeRtew2qeam8OzERXPw "semicolons on top"). Also as reference:  [AirBnB style](https://intranet.hbtn.io/rltoken/D8wEPwvtilCjNqotmoSruw "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   You are not allowed to use  `var`

## More Info

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://intranet.hbtn.io/rltoken/_6jQeRtew2qeam8OzERXPw "Documentation")

```
$ sudo npm install semistandard --global
```