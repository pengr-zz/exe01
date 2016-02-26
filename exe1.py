import exe2

import sys 
import os

print __file__

from exe2 import fuc2
from exe3 import fuc3

def fuc1():
    print "hello world!"
    fuc2()
    fuc3()

if __name__=="__main__":
    fuc1()
