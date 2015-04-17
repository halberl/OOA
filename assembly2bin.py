'''
Filename: assembly2Bin.py
Author: Lucas Halbert
Date:   04/17/15
Description: This utility will encode assembly instructions to binary 
             and store in the specified file.
'''
import sys
from classes.encode import INSTRUCTIONEncode

# Get filename
filename = input("Please enter a filename to store instructions:")

# Open file for writing
f = open(filename, 'w')

print("To exit this program, write 'quit'")
while 1:
    instruction = input("Please Enter Instruction: ")
    if instruction == "quit":
        f.close
        sys.exit(0)
    print("The entered text is: ",instruction)

    a=INSTRUCTIONEncode(instruction)
    a.encodeOpField()
    a.encodeDestField()
    a.encodeSource1Field()
    if a.immediate == 0:
        a.encodeSource2Field()
    elif a.immediate == 1:
        a.encodeImmediateValue()
    a.constructByteCode()

    print(a.inst_bin)
    f.write(a.inst_bin + '\n')

#print(a.inst_bin, file=filename)


