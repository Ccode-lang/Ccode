## Ccode
A new, fast, and statically typed language that compiles to javascript.  
Ccode has nothing to do with C, it is a separate project.  
Go to the Discussions page to get help on how to use it!
## The package manager is now fully functional!
If you have questions open an issue.  
Also look at https://github.com/Ccode-lang/Ccode/wiki/package-manager.
## Supported platforms
 * Linux
 * Macos
 * Windows (using WSL. No plan to implement normal windows.)
## Installing third-party modules
 * Download with reppack
## Contributing
Please send in pull requests to get your features here.

## How it works
1. It first creates main.js and imports the builtin module.
2. It reads a file given to it and gets rid of whitespace such as tabs or spaces at the start or end of a command.
3. Once it reads all the lines it runs the Javascript it created.
4. It deletes the Javascript.
## setup (without Ccode Command addon)
```bash
cd ~
git clone https://github.com/Ccode-lang/Ccode.git
cd Ccode
make all
```
## Running (without Ccode command addon)
```bash
# python3
python3 Ccode.py <path to Ccode file>
```
## With Ccode command addon
```
Ccode <file.cc> <args to pass>
```

## Requirments
1. Python 3 (To run the compiler)
2. Bash (You need to be on Linux for it to work so this is installed)
3. Node.js 14-15 (To run the Javascript files that are generated)
4. NPM (for packages)


## Installation
Go to https://github.com/Ccode-lang/Ccode-Command and follow the instructions there.
> this may be out of sync!  
## Uninstalling
Ccode can be completely uninstalled by removing the `~/Ccode` directory.
Ccode (and its module) is completely contained in the `~/Ccode` directory.  If you have the `Ccode-command` addon you will have to uninstall that separately.
## Find out how to use it
See [here](https://github.com/Ccode-lang/Ccode/wiki/builtins-and-basic-use)
## Please record issues to get them fixed or go to discussion if you get an error message!
This language is in early stages of development.  
If you get a node.js error message it means you either forgot an end bracket, parenthesis, forgot to execute a command, didn't execute a command right, or there is an error in the main Ccode.py file.  
If you get errors like these report them as soon as possible.  


