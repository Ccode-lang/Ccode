#imports and settings
import os
running = True
os.system("cp ~/Ccode/scripts/main.js ~/Ccode/")

#js writing command
def js(out):
    f = open("main.js", "a")
    f.write("\n")
    f.write(out)
    f.close()

#unknown command message
def NU():
    print("unknown command")

#loop start
while running:
    #input
    inp = input("Ccode language >> ")
    #print
    if inp.startswith("print "):
        println = inp.replace("print ", "")
        out = "console.log(" + println + ");"
        js(out)
    #run
    elif inp == "run":
        running = False
    #if statements
    elif inp.startswith("if ") and inp.endswith(" {"):
        out = inp.replace("if ", "")
        out = out.replace(" {", "")
        js("if (" + out + ") {")
    #end brackets
    elif inp == "}":
        js(inp)
    #variables
    elif inp.find("=") > -1 or inp.find(" = ") > -1:
        out = inp
        if inp.find("input") > -1:
            out = inp.replace("input", "prompt('>>')")
        js(out + ";")
    else:
        NU()
#end of loop

#run commands
os.system("./run")
os.system("rm main.js")
