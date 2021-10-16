#imports and settings
import os
import sys
#check if the directory is a node project
node = os.path.exists("main.js") or os.path.exists("node_modules") or os.path.exists("package.json") or os.path.exists("lib")
if os.getcwd().endswith("Ccode"):
    node = True
#js writing command
def js(out):
    #If dir is node project don't write to temp.js
    if not node:
        f = open("temp.js", "a")
        f.write("\n")
        f.write(out)
        f.close()
    else:
        return
#copy project to current dir unless it is a node project
if not node:
    os.system("cp -r ~/Ccode/node_modules .")
    os.system("cp ~/Ccode/package.json .")
    os.system("cp ~/Ccode/package-lock.json .")
    os.system("cp -r ~/Ccode/lib .")
else:
    print("\n\nPlease don't run in node project folders.  Project will be scanned for errors but not run.\n\n")
#make temp.js
if not node:
    os.system("touch temp.js")
# input import
js("const input = require('prompt-sync')();")
# builtins
builtins = open("lib/builtins/builtins.js", "r")
data = builtins.read()
builtins.close()
js(data + "\n")
builtin_commands = open("lib/builtins/com.txt", "r")
commands = builtin_commands.read()
builtin_commands.close()
args = sys.argv
#load script file
try:
    file = open(args[1], 'r')
    text = file.readlines()
    file.close()
except:
    print("\n\n\n\nFile " + args[1] + " missing, aborting\n\n\n\n")
    if not node:
        os.system("rm -r node_modules")
        os.system("rm package.json")
        os.system("rm package-lock.json")
        os.system("rm temp.js")


#unknown command message
def NU(line):
    print("error on line: " + str(line))
line_num = 0
#loop start
for line in text:
    line_num += 1
    #input
    inp = line.strip()
    #comments
    if inp == "" or inp.startswith("//"):
        out = "null"
    #imports
    elif inp.startswith("import "):
        imp = inp[7:]
        #get file
        try:
            impfile = open("lib/" + imp + "/" + imp + ".js", "r")
            data = impfile.read()
            impfile.close()
            js(data + "\n")
            comfile = open("lib/" + imp + "/com.txt", "r")
            newcoms = comfile.read()
            comfile.close()
            commands = commands + newcoms
        except:
            print(f'module "{imp}" does not exist')
    #functions
    elif inp.startswith("func ") and inp.endswith(" {"):
        out = inp.replace("func ", "function ")
        out = out.replace("{", "")
        js(out + "{")
    #while
    elif inp.startswith("while ") and inp.endswith(" {"):
        out = inp.replace("while ", "")
        out = out.replace(" {", "")
        js("while (" + out + ") {")
    #if statements
    elif inp.startswith("if ") and inp.endswith(" {"):
        out = inp.replace("if ", "")
        out = out.replace(" {", "")
        js("if (" + out + ") {")
    #else
    elif inp == "else {":
        js(inp)
    #elif
    elif inp.startswith("elif ") and inp.endswith(" {"):
        out = inp.replace("elif ", "")
        out = out.replace(" {", "")
        js("else if (" + out + ") {")
    #end brackets
    elif inp == "}":
        js(inp)
    #variables
    elif inp.find("=") > -1 or inp.find(" = ") > -1:
        if inp.startswith("set "):
            change = inp.replace("set ", "")
            out = "var " + change
        else:
            out = inp
        try:
            out = out.replace("input", "input('>>')")
        except:
            out = out
        js(out + ";")
    #function execution
    elif inp.endswith(")"):
        if inp.split("(")[0] in commands:
            js(inp)
        else:
            print("unknown command")
            NU(line_num)
            break
    #errors
    else:
        NU(line_num)
#end of loop
#if project is node directory don't delete node files or run node project made
if not node:
    os.system("node temp.js")
    os.system("rm temp.js")
    os.system("rm -r node_modules")
    os.system("rm package.json")
    os.system("rm package-lock.json")
    os.system("rm -r lib")
