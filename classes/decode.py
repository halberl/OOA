'''
Filename: decode.py
Author:   Lucas Halbert
Date:     4/17/15
Modified: 4/17/15
Description: decodes binary to assembly 
'''
import sys
import re
import json
import hw

'''
Class declarations for each stage of the pipeline
'''
class INSTRUCTIONDecode(object):
    '''
    This class is used to decode instructions passed to it. The instruction dictionary
    contains all specific bit mappings for each instruction operand. 
    '''

    def __init__(self, instruction, data_reg):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        # Read and Open dictionary file relative to root of project
        self.inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())

        # Initialize instuction
        self.instruction = instruction
        
        # Initialize data register
        self.data_reg = data_reg

        #print("Instruction:",self.instruction)


    def decodeField0(self):
        '''
        This constructor decodes the OP field of the instruction.
        '''
        # Extract the first 5 characters of the binary instruction
        inst_op_bin = self.instruction[:5]
        print("Instruction Op Binary:", inst_op_bin)

        # Lookup the operation of the extracted binary
        self.inst_op = self.inst_dict[inst_op_bin]
        print("Instruction Op:",type(self.inst_op),self.inst_op)
        
        # Check if last character of Operator specifies immediate value
        if self.inst_op[len(self.inst_op)-1] == "i":
            self.immediate = 1
        else:
            self.immediate = 0
        #print("Immediate?:",self.immediate)

        #return self.inst_op


        #########################
        #   Memory Operations   #
        #########################
        if (self.inst_op == "ld") or (self.inst_op == "st") or (self.inst_op == "move") or (self.inst_op == "swap"):
            '''
            Memory Operation Structure
            |-----------------------|
            |  OP  , dest , source  |
            |  ld  ,  $1  ,  0($2)  |
            |-----------------------|
            |  OP  , source , dest  |
            |  st  ,  $1    , 0($2) |
            |-----------------------|
            |  OP  , dest , source  |
            | move ,  $1  ,  0($2)  |
            |-----------------------|
            |  OP  , dest ,  dest   |
            | swap ,  $1  ,  0($2)  |
            |-----------------------|
            '''
            # Decode Destination Field
            destination = self.decodeField1()

            # Decode Mem operation
            source = self.decodeMem()
            print("Source",source)

            # split source into index and source register address
            index = int(source.split("(")[0])
            print(source.split("(")[1].split(")")[0].split("$")[1])
            source = int(source.split("(")[1].split(")")[0].split("$")[1])
            
            # fetch register value and convert to int
            print("reg address",source)
            mem_address = int(self.data_reg[source].read(), 2)

            # add index to memory address
            self.mem_address = (index + mem_address)
            print(mem_address)

        #########################
        # Arithmetic Operations #
        #########################
        elif (self.inst_op == "add") or (self.inst_op == "sub") or (self.inst_op == "mul") or (self.inst_op == "div"):
            '''
            Arithmetic Operation Structure
            |-----------------------|
            | OP  , dest , source  |
            | add ,  $1  ,  0($2)  |
            |-----------------------|
            | OP  , source , dest  |
            | sub  ,  $1    , 0($2) |
            |-----------------------|
            | OP  , dest , source  |
            | mul ,  $1  ,  0($2)  |
            |-----------------------|
            |  OP  , dest ,  dest   |
            | swap ,  $1  ,  0($2)  |
            |-----------------------|
            '''
#            self.add()
#        elif self.inst_op == "sub":
#            self.sub()
#        elif self.inst_op == "mul":
#            self.mul()
#        elif self.inst_op == "div":
#            self.div()
#        elif self.inst_op == "addi":
#            self.addi()
#        elif self.inst_op == "subi":
#            self.subi()
#        elif self.inst_op == "muli":
#            self.muli()
#        elif self.inst_op == "divi":
#            self.divi()
#        elif self.inst_op == "and":
#            self.and1()
#        elif self.inst_op == "or":
#            self.or1()
#        elif self.inst_op == "not":
#            self.not1()
#        elif self.inst_op == "nand":
#            self.nand()
#        elif self.inst_op == "nor":
#            self.nor()
#        elif self.inst_op == "beq":
#            self.beq()
#        elif self.inst_op == "bne":
#            self.bne()
#        elif self.inst_op == "bez":
#            self.bez()
#        elif self.inst_op == "bnz":
#            self.bnz()
#        elif self.inst_op == "bgt":
#            self.bgt()
#        elif self.inst_op == "blt":
#            self.blt()
#        elif self.inst_op == "bge":
#            self.bge()
#        elif self.inst_op == "ble":
#            self.ble()


########################################################

        


    def decodeField1(self):
        '''
        This constructor decodes the destination field of the instruction
        '''
        # Extract the next 5 characters of the binary instruction
        self.inst_dest_bin = self.instruction[5:10]
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(self.inst_dest_bin, 2) > 31:
            print("Register",int(self.inst_dest_bin, 2),"does not exist")
            sys.exit(4)


        # Convert the extracted binary to a register number
        self.inst_dest = "$" + str(int(self.inst_dest_bin, 2))
        print("Instruction Dest:",self.inst_dest)

        return self.inst_dest


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

        return self.inst_source1


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

        return self.inst_source2


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

        return self.inst_immediate


    def decodeMem(self):
        '''
        This constructor decodes the index and register location for a memory operation
        '''
        # Extract characters 11-27 of binary as index
        source_index_bin = self.instruction[11:27]
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(source_index_bin, 2) > 131071:
            print("Cannot use index numbers large than 131071")
            sys.exit(4)

        # Convert extracted binary to an int
        source_index = str(int(source_index_bin, 2)) + "("
        
        # Extract characters 28-32 of binary as source register
        source_reg_bin = self.instruction[28:32]

        # Convert extracted binary to a register number
        source_reg = "$" + str(int(source_reg_bin, 2)) + ")"

        # Combine index and register number
        source = source_index + source_reg

        print("mem operation decode:", source)

        return source


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

        return self.inst
