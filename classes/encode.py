#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Filename: encode.py
Author:   Lucas Halbert
Date:     4/16/15
Modified: 4/17/15
Description: Encodes instructions passed to it via assembly2Bin.py to the instructions
             binary representation and writes it out to the specified file.
'''
import sys
import re
import json

class INSTRUCTIONEncode(object):
    '''
    This class is used to encode instructions passed to it. The instruction dictionary
    contains all specific bit mappings for each instruction operand. 
    '''

    def __init__(self, instruction):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        print("Being encoding inst: ", instruction)
        # Read and Open dictionary file relative to root of project
        self.inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())
        # Swap keys and values of dictionary
        self.inst_dict = dict(zip(self.inst_dict.values(),self.inst_dict.keys()))
        # Initialize instuction
        self.instruction = instruction
        #print("Instruction:",self.instruction)

        # Split instruction by "," and store in inst_fields
        self.inst_fields = self.instruction.split(',')
        #print("Instruction Fields:",self.inst_fields)

        self.field_array = [None]*5
        self.field_array[0] = self.encodeOpField()
        self.op_type = self.op_type()
        self.field_array[1] = self.encodeRegister(1)

        print("Op type is ", self.op_type)
        # 1 is memory operation
        if (self.op_type == 1):
            # 3rd field is 
            # 4th field is memory address
            self.encodeMemory()
        # 2 is memory operation immediate
        elif (self.op_type == 2):
            # 3rd field is immediate index value
            # 4th field is memory address
            self.field_array[2] = "00000"
            self.field_array[3] = self.encodeMemoryImmediate()
        

        # 3 is arithmatic operation
        elif (self.op_type == 3):
            # 3rd field is first source register
            # 4th field is second source register
            self.field_array[2] = self.encodeRegister(2)
            self.field_array[3] = self.encodeRegister(3)

        # 4 is arithmatic immediate operation
        elif (self.op_type == 4):
            # 3rd field is source register
            # 4th field is immediate value
            self.field_array[2] = self.encodeRegister(2)
            self.field_array[3] = self.encodeImmediate(3)

        # 5 is branch operation
        elif (self.op_type == 5):
            # 3rd field is source register
            # 4th field is 2nd source register
            self.field_array[2] = self.encodeRegister(2)
            self.field_array[3] = self.encodeRegister(3)

        print("0 = ", self.field_array[0])
        print("1 = ", self.field_array[1])
        print("2 = ", self.field_array[2])
        print("3 = ", self.field_array[3])
        print("Instruction encoded= ", self.constructByteCode())

        #return self.constructByteCode()

    def encodeImmediate(self, index):
        #
        if int(self.inst_fields[index].split('#')[1]) > 13171:
            print("Immediate", self.inst_fields[index],"is too big")
            sys.exit(4)
        
        return "{0:b}".format(int(self.inst_fields[index].split('#')[1])).rjust(17, '0')

    def encodeRegister(self, index):
        if int(self.inst_fields[index].split('$')[1]) > 31:
            print("Register", self.inst_fields[index],"does not exist")
            sys.exit(4)
        
        return "{0:b}".format(int(self.inst_fields[index].split('$')[1])).rjust(5, '0')

    def encodeMemory(self):
        self.field_array[2] = self.inst_fields[2].split("(")[0].rjust(17, '0')
        self.field_array[3] = self.inst_fields[2].split("(")[1].split(")")[0].split("$")[1].rjust(5, '0')

        index_bin = "{0:b}".format(int(self.field_array[2])).rjust(17, '0')
        reg_bin= "{0:b}".format(int(self.field_array[3])).rjust(5, '0')
        return index_bin+reg_bin

    def encodeMemoryImmediate(self):

        return "{0:b}".format(int(self.inst_fields[2].split('#')[1])).rjust(17, '0')








    def encodeOpField(self):
        '''
        This constructor encodes the OP field of the instruction.
        '''

        # Extract Instruction Operator from field 0
        self.inst_op = self.inst_fields[0]

        # Check if 4th character of Operator specifies immediate value
        if self.inst_op[len(self.inst_op)-1] == "i":
            self.immediate = 1
        else:
            self.immediate = 0
        #print("Immediate?:",self.immediate)

        self.inst_op_bin = self.inst_dict[self.inst_fields[0]]
        
        #print("Instruction OP:",self.inst_fields[0])
        #print("Instruction OP Binary:",self.inst_op_bin)

        return self.inst_op_bin



        #encodeDestField()



    def op_type(self):

        self.inst_op = self.inst_fields[0]
        #########################
        #   Memory Operations   #
        #########################
        if (self.inst_op == "ld") or (self.inst_op == "st") or (self.inst_op == "move") or (self.inst_op == "swap"):
            self.op_type = 1

        ########################
        # Immediate Memory Operations #
        ########################
        elif (self.inst_op == "ldi") or (self.inst_op == "sti"):
            self.op_type = 2

        #########################
        #   Arithmatic Operations   #
        #########################
        elif (self.inst_op == "add") or (self.inst_op == "sub") or (self.inst_op == "mul") or (self.inst_op == "div"):
            self.op_type = 3

        ###################################
        # Immediate Arithmetic Operations #
        ###################################
        elif (self.inst_op == "addi") or (self.inst_op == "subi"):
            self.op_type = 4

        #########################
        #   Logical Operations   #
        #########################
        #if (self.inst_op == "ld") or (self.inst_op == "st") or (self.inst_op == "move") or (self.inst_op == "swap"):
            #


        #########################
        #   Branch Operations   #
        #########################
        if (self.inst_op == "ld") or (self.inst_op == "st") or (self.inst_op == "move") or (self.inst_op == "swap"):
            self.op_type = 5
            
        return self.op_type           



    def encodeDestField(self):
        '''
        This constructor encodes the destination field of the instruction
        '''

        # Extract instruction destination from field 1
        self.inst_dest = self.inst_fields[1]

        # Error check to confirm that field 1 does not contain a register that does not exist(>31)
        if int(self.inst_dest.split('$')[1]) > 31:
            print("Register",self.inst_dest,"does not exist")
            sys.exit(4)

        # Convert instruction destination to binary and pad to 5 bits MSB
        self.inst_dest_bin = "{0:b}".format(int(self.inst_fields[1].split('$')[1])).rjust(5, '0')
        #print("Instruction Destination:",self.inst_dest)
        #print("Instruction Dest Binary:",self.inst_dest_bin)

        return self.inst_dest_bin


    def encodeSource1Field(self):
        '''
        This constructor encodes the source1 field of the instruction
        '''

        # Extract instruction source1 from field 2
        self.inst_source1 = self.inst_fields[2]

        # Error check to confirm that field 2 does not contain a register that does not exist(>31)
        if int(self.inst_source1.split('$')[1]) > 31:
            print("Register",self.inst_source1,"does not exist")
            sys.exit(4)

        # Convert instruction source1 to binary and pad to 5 bits MSB
        self.inst_source1_bin = "{0:b}".format(int(self.inst_fields[2].split('$')[1])).rjust(5, '0')
        #print("Instruction Source1:",self.inst_source1)
        #print("Instruction source1 Binary:",self.inst_source1_bin)

        return self.inst_source1_bin


    def encodeSource2Field(self):
        '''
        This constructor encodes the source2 field of the instruction
        '''

        # Extract instruction source1 from field 3
        self.inst_source2 = self.inst_fields[3]

        # Error check to confirm that field 3 does not contain a register that does not exist(>31)
        if int(self.inst_source2.split('$')[1]) > 31:
            print("Register",self.inst_source2,"does not exist")
            sys.exit(4)

        # Convert instruction source2 to binary and pad to 5 bits MSB
        self.inst_source2_bin = "{0:b}".format(int(self.inst_fields[3].split('$')[1])).rjust(5, '0')
        #print("Instruction Source2:",self.inst_source1)
        #print("Instruction source2 Binary:",self.inst_source2_bin)

        return self.inst_source2_bin


    def encodeImmediateValue(self):
        '''
        This constructor decodes the immediate value field of the instruction if self.immediate = 1
        '''

        # Extract instruction immediate value from field 3
        self.inst_immediate = self.inst_fields[3]


        # Error check to confirm that field 3 does not contain a register that does not exist(>31)
        if int(self.inst_immediate.split('#')[1]) > 131071 :
            print("Values greater than 131071 cannot be entered")
            sys.exit(5)

        # Convert instruction immediate value to binary and pad to 17 bits LSB 
        self.inst_immediate_bin = "{0:b}".format(int(self.inst_fields[3].split('#')[1])).rjust(17, '0')
        #print("Instruction Immediate:",self.inst_immediate)
        #print("Instruction Immediate Binary:",self.inst_immediate_bin)

        return self.inst_immediate_bin


    def constructByteCode(self):
        '''
        This constructor compiles all of the binary fields into a single 32 bit binary string to be passed
        to other stages of the pipeline.
        '''

        # Combine OP, Dest, Source1, and Source2 into compiled binary
        #if self.immediate == 1:
            #self.inst_bin = self.inst_op_bin + self.inst_dest_bin + self.inst_source1_bin + self.inst_immediate_bin
        #elif self.immediate == 0:
            #self.inst_bin = self.inst_op_bin + self.inst_dest_bin + self.inst_source1_bin + self.inst_source1_bin

        print(self.field_array[0] + self.field_array[1] + self.field_array[2] + self.field_array[3])
        self.inst_bin = self.field_array[0] + self.field_array[1] + self.field_array[2] + self.field_array[3]
        self.inst_bin_len = len(self.inst_bin)

        #print("Instruction Length:",len(self.inst_bin))

        # Force 32 bit length
        self.inst_bin = self.inst_bin.ljust(32, '0')
        #print("Instruction Length:",len(self.inst_bin))
        #print("Complete Instruction Binary:",self.inst_bin)

        return self.inst_bin



