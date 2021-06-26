## Ccode
A new, fast, and lightweight language that compiles to javascript.  
Ccode has nothing to do with any other version of C, it is a separate project.

## Contributing
Please send in pull requests to get your features here.

## How it works
1. It first creates main.js and imports input lines.
2. It reads a file given to it and gets rid of whitespace such as tabs or spaces at the start or beginning of a command.
3. Once it reads all the lines it runs the Javascript it created.
4. It deletes the Javascript. (Comment the last line to turn this off, if turned off it may cause errors)

## Running
```bash
# python3
python3 Ccode.py <path to Ccode file>

# python2
python Ccode.py <path to Ccode file>
```

## Requirments
1. Python3 or 2 (To run the compiler)
2. Bash (You need to be on linux for it to work so this is installed)
3. Node.js (To run the Javascript files that are generated)


## Installation
```bash
command cd ~/
git clone https://github.com/Ccode-lang/Ccode.git
cd Ccode/
make all
```
### Output from ```make all```
```
Installing npm deps...

added 3 packages, and audited 4 packages in 1s

found 0 vulnerabilities
Done

Testing...
running hello world...




Please don't run in node project folders


hello world
```
## Install as command
Go to https://github.com/Ccode-lang/Ccode-Command and follow the instructions there to install it as a command.  
Then use the command ```Ccode <Ccode file>``` instead of ```python3 path/to/Ccode.py <Ccode file>```
## Included commands
### Print syntax: 
```
print 'hi'
```
### Variables syntax1: 
```
set h = 5
```
#### syntax2:
```
h = 5
```
### If statements syntax: 
```
if h == 5 {  
print 'hi'  
}  
elif h == 4 {   
print 'bye'  
}  
else {  
print 'hello'  
}  
```
### Input variable syntax: 
```
h = input
```
This gets user input and stores it in the given variable.
### While
```
while h == 1 {  
print 'hi'  
}  
```
### Functions
Declaration
```
func test(num1, num2) {
  print num1 + num2
}
```
Using function
```
test(1, 2)
```

### Comments
```
// This is a comment
```

## Please record issues to get them fixed or go to discussion if you get an error message!
This language is in early stages of development.  
If you get a node.js error message it means you either forgoten a end bracket, parenthesis, forgot to execute a command, didn't execute a command right, or there is an error in the main Ccode.py file.  
If you get errors like these report them as soon as possible.  


