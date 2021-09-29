def output (s):
    print (s)

def fatalError ():
    print ("FATAL ERROR");
    
def C (x):
    if (x == "q"):
        output ("v")
    elif (x == "r"):
        output ("w")
    elif (x == "s"):
        output ("x")
    elif (x == "t"):
        output ("y")
    elif (x == "u"):
        output ("z")
    else:
        fatalError ()

def B (x):
    if (x == "q"):
        C ("s")
    elif (x == "r"):
        C ("t")
    else:
        fatalError ()
        
def codeV1 ():
    B ("q")
    C ("q")

def codeV2 ():
    C ("q")
    B ("q")

print ("Version 1")
codeV1()
print ("Version 2")
codeV2 ()

    
