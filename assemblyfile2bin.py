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

class FileToBin:
    def __init__(self, sourcefile, binfile):
        self.sourcefile = sourcefile
        self.binfile= binfile
        self.bin_array = []
        self.instructions=[]
        print ("\nFinished init of FileToBin")

    
    def read(self):
         f = open(self.sourcefile, 'r')
         with open(self.sourcefile) as f:
             self.instructions = f.readlines()
         
         f.close()



    def write(self):

        # Open file for writing
        f = open(self.binfile, 'w')
        
        #while :
        for inst in self.instructions:
            if inst== "quit":
                # Close file to free up system resources
                f.close
                # Exit gracefully
                sys.exit(0)
        
            # Call INSTRUCTIONEncode class
            a=INSTRUCTIONEncode(inst)
        
            # Encode operation field
            #a.encodeOpField()
        
            # Encode destination field
            #a.encodeDestField()
        
            # Encode source1 field
            #a.encodeSource1Field()
        
            #if a.immediate == 0:
                # Encode source2 field
                #a.encodeSource2Field()
            #elif a.immediate == 1:
                # Encode immediate value field
                #a.encodeImmediateValue()
        
            # Construct binary representation of instruction
            #a.constructByteCode()
        
            # Print constructed byte code
            #print(a.inst_bin)
        
            # return data to call
            self.bin_array.append(a.inst_bin)

            # Write byte code to file with newline
            f.write(a.inst_bin + '\n')
        
        f.close()

        return self.bin_array
