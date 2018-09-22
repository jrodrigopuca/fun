# $python 11.py -f test.txt
#
# Crea un log sobre el archivo
# 
import sys, getopt, os, datetime

def addLog(myfile):
    mydir= os.path.dirname(os.path.abspath(__file__))
    file = open(myfile,"a")
    file.write(str(datetime.datetime.now())+"\n")
    file.close()


def getArgs(fArgs):
    ops, args= getopt.getopt(fArgs,"f:","file=") 
    for op, arg in ops:
        if op =="-f":
            addLog(arg)       
            print ("is OK",arg)
              
if __name__ == "__main__":
    getArgs(sys.argv[1:])
    