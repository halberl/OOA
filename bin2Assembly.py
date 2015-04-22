#!/usr/local/env python3
# -*- coding: utf-8 -*-
'''
Filename: bin2Assembly.py
Author: Lucas Halbert
Date:   04/17/15
Modified: 04/21/15
Description: This utility reads binary assembly instructions from the specified 
             file and decode to readable assembly instructions.
'''
import sys
import os.path
from classes.decode import INSTRUCTIONDecode

# initialize filename to nothing
filename=''
# check if file exists
while not os.path.isfile(filename):
    # Get filename
    filename = input("Please enter a filename to read instructions:")
    # Query user again if file does not exist
    if not os.path.isfile(filename):
        print("The file",filename,"does not exist")


# Open file for reading
f = open(filename, 'r')


# Loop through lines of the file and read them
for binary in f:
    print(binary, end="")

    # Call INSTRUCTIONDecode class
    a=INSTRUCTIONDecode(binary)

    # Decode operation field
    a.decodeOpField()

    # Decode destination field
    a.decodeDestField()

    # Decode source1 field
    a.decodeSource1Field()

    if a.immediate == 0:
        # Decode source2 field
        a.decodeSource2Field()
    elif a.immediate == 1:
        # Decode immediate value field
        a.decodeImmediateValue()

    # Construct instruction
    a.constructInstruction()

    # Print full instruction
    print(a.inst)

# Close file to free up system resources
f.close

# Exit gracefully
sys.exit(0)
