'''
Filename: decode.py
Author:   Lucas Halbert
Date:     4/17/15
Modified: 4/17/15
Comment:  
'''
import sys
import re
import json

#NEEDS TO FLAG HAZARDS

'''
Class declarations for each stage of the pipeline
'''
class INSTRUCTIONDecode(object):
    '''
    This class is used to fetch an instructions from the instruction memory and place it 
    into the instruction register for decoding.
    '''

    def __init__(self, location):
        '''
        This constructor initializes
        '''

    def fetchFromMem(self):
        '''
        '''
        # Open instruction memory object and fetch the instruction pointed to by the stack pointer

        # Place the fetched instruction in the instruction register




class INSTRUCTIONDecode(object):
    '''
    This class is used to decode instructions passed to it. The instruction dictionary
    contains all specific bit mappings for each instruction operand. 
    '''

    def __init__(self, instruction):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        # Read and Open dictionary file relative to root of project
        self.inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())
        # Initialize instuction
        self.instruction = instruction
        #print("Instruction:",self.instruction)


    #def splitFields(self):
        '''
        This constructor splits the instruction string into usable fields.
        '''
        # Split instruction by "," and store in inst_fields
        #self.inst_fields = self.instruction.split(',')
        #print("Instruction Fields:",self.inst_fields)
        #return self.inst_fields


    def decodeOpField(self):
        '''
        This constructor decodes the OP field of the instruction.
        '''
        # Extract the first 5 characters of the binary instruction
        self.inst_op_bin = self.instruction[:5]
        #print("Instruction Op Binary:",self.inst_op_bin)

        # Lookup the operation of the extracted binary
        self.inst_op = self.inst_dict[self.inst_op_bin]
        #print("Instruction Op:",self.inst_op)
        
        # Check if last character of Operator specifies immediate value
        if self.inst_op[len(self.inst_op)-1] == "i":
            self.immediate = 1
        else:
            self.immediate = 0
        #print("Immediate?:",self.immediate)


    def decodeDestField(self):
        '''
        This constructor decodes the destination field of the instruction
        '''
        # Extract the next 5 characters of the binary instruction
        self.inst_dest_bin = self.instruction[5:10]
        #print("Instruction Dest Binary:",self.inst_dest_bin)
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(self.inst_dest_bin, 2) > 31:
            print("Register",int(self.inst_dest_bin, 2),"does not exist")
            sys.exit(4)


        # Convert the extracted binary to a register number
        self.inst_dest = "$" + str(int(self.inst_dest_bin, 2))
        #print("Instruction Dest:",self.inst_dest)


    def decodeSource1Field(self):
        '''
        This constructor decodes the source1 field of the instruction
        '''
        # Extract the next 5 characters of the binary instruction
        self.inst_source1_bin = self.instruction[10:15]
        #print("Instruction Source1 Binary:",self.inst_source1_bin)
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(self.inst_source1_bin, 2) > 31:
            print("Register",int(self.inst_source1_bin, 2),"does not exist")
            sys.exit(4)

        # Convert the extracted binary to a register number
        self.inst_source1 = "$" + str(int(self.inst_source1_bin, 2))
        #print("Instruction Dest:",self.inst_source1)


    def decodeSource2Field(self):
        '''
        This constructor decodes the source2 field of the instruction
        '''
        # Extract the next 5 characters of the binary instruction
        self.inst_source2_bin = self.instruction[15:20]
        #print("Instruction Source2 Binary:",self.inst_source2_bin)
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(self.inst_source2_bin, 2) > 31:
            print("Register",int(self.inst_source2_bin, 2),"does not exist")
            sys.exit(4)

        # Convert the extracted binary to a register number
        self.inst_source2 = "$" + str(int(self.inst_source2_bin, 2))
        #print("Instruction Dest:",self.inst_source2)


    def decodeImmediateValue(self):
        '''
        This constructor decodes the immediate value field of the instruction if self.immediate = 1
        '''
        # Extract the next 5 characters of the binary instruction
        self.inst_immediate_bin = self.instruction[15:31]
        #print("Length:",len(str(self.inst_immediate_bin)))
        #print("Instruction Immediate Binary:",self.inst_immediate_bin)
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(self.inst_immediate_bin, 2) > 131071:
            print("Cannot use numbers large than 131071")
            sys.exit(4)

        # Convert the extracted binary to a register number
        self.inst_immediate = "#" + str(int(self.inst_immediate_bin, 2))
        #print("Immediate Value:",self.inst_immediate)


    def constructInstruction(self):
        '''
        This constructor compiles all of the binary fields into a single 32 bit binary string to be passed
        to other stages of the pipeline.
        '''

        # Combine OP, Dest, Source1, and Source2 into compiled binary
        if self.immediate == 1:
            self.inst = self.inst_op + "," + self.inst_dest + "," + self.inst_source1 + "," + self.inst_immediate
        elif self.immediate == 0:
            self.inst = self.inst_op + "," + self.inst_dest + "," + self.inst_source1 + "," + self.inst_source1

        #print("Instruction Length:",len(self.inst))
        print("Complete Instruction:",self.inst)
