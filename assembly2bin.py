#!/usr/local/env python3
# -*- coding: utf-8 -*-
'''
Filename: assembly2Bin.py
Author: Lucas Halbert
Date:   04/17/15
Modified: 04/21/15
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
    # Query user for instruction
    instruction = input("Please Enter Instruction: ")
    if instruction == "quit":
        # Close file to free up system resources
        f.close
        # Exit gracefully
        sys.exit(0)

    # Call INSTRUCTIONEncode class
    a=INSTRUCTIONEncode(instruction)

    # Encode operation field
    a.encodeOpField()

    # Encode destination field
    a.encodeDestField()

    # Encode source1 field
    a.encodeSource1Field()

    if a.immediate == 0:
        # Encode source2 field
        a.encodeSource2Field()
    elif a.immediate == 1:
        # Encode immediate value field
        a.encodeImmediateValue()

    # Construct binary representation of instruction
    a.constructByteCode()

    # Print constructed byte code
    print(a.inst_bin)

    # Write byte code to file with newline
    f.write(a.inst_bin + '\n')



