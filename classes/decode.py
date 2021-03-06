'''
Filename: decode.py
Author:   Lucas Halbert
Date:     4/17/15
Modified: 4/29/15
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

    def __init__(self, instruction, data_reg, WB_addr, ALU_in, ALU_out):
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
        
        # Initialize Write Back address
        self.WB_addr = WB_addr

        # Create ALU_IN array
        self.ALU_in = []

        #print("Instruction:",self.instruction)

        # Start the decode process
        self.decodeField0()
        print("decode-self.ALU_in",self.ALU_in)
        #return self.ALU_in


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
        #if self.inst_op[len(self.inst_op)-1] == "i":
        #    self.immediate = 1
        #else:
        #    self.immediate = 0
        #print("Immediate?:",self.immediate)

        #return self.inst_op

        # Append instruction operation to ALU_in as element 0
        self.ALU_in.append(self.inst_op)


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
            destination = int(self.decodeField1().split("$")[1])

            # Decode Mem operation
            source = self.decodeMem()
            print("Source",source)

            # split source into index and source register address
            index = int(source.split("(")[0], 2)
            print("source?:",source.split("(")[1].split(")")[0].split("$")[1])
            source = int(source.split("(")[1].split(")")[0].split("$")[1])
            
            # fetch register value and convert to int
            print("reg address",source)
            mem_address = int(self.data_reg[source].read(), 2)

            # add index to memory address
            self.mem_address = (index + mem_address)
            print(self.mem_address)

            # Append destination register to ALU_in as element 1
            self.ALU_in.append(destination)
            # Append index to ALU_in as element 2
            self.ALU_in.append(index)
            # Append source to ALU_in as element 3
            self.ALU_in.append(source)


        ########################
        # Immediate Operations #
        ########################
        elif (self.inst_op == "ldi") or (self.inst_op == "sti"):
            '''
            Immediate Operation Structure
            |-------------------------|
            |  OP  , dest , Immediate |
            | ldi  ,  $2  ,  #34266   | 
            |-------------------------|
            '''
            # Decode Destination Field
            destination = int(self.decodeField1().split("$")[1])

            # Decode Immediate operation
            immediate = int(self.decodeImmediateValue().split("#")[1])


            # Append destination register to ALU_in as element 1
            self.ALU_in.append(destination)
            # Append immediate value to ALU_in as element 2
            self.ALU_in.append(immediate)


        #########################
        # Arithmetic Operations #
        #########################
        elif (self.inst_op == "add") or (self.inst_op == "sub") or (self.inst_op == "mul") or (self.inst_op == "div"):
            '''
            Arithmetic Operation Structure
            |--------------------------|
            | OP  , dest , src1 | src2 |
            | add ,  $1  ,  $2  |  $3  |
            |--------------------------|
            | OP  , dest , src1 | src2 |
            | sub  , $1  ,  $2  |  $3  |
            |--------------------------|
            | OP  , dest , src1 | src2 |
            | mul ,  $1  ,  $2  |  $3  |
            |--------------------------|
            | OP  , dest , src1 | src2 |-----> Remainder placed in remainder register???
            | div ,  $1  ,  $2  |  $3  |
            |--------------------------|
            '''
            # Decode Destination Field
            destination = int(self.decodeField1().split("$")[1])

            # Decode Source 1 & 2 Fields
            source1 = int(self.decodeSource1Field().split("$")[1])
            source2 = int(self.decodeSource2Field().split("$")[1])
            
            # Print everything 
            print(self.inst_op,destination,source1,source2)


            # Append destination register to ALU_in as element 1
            self.ALU_in.append(destination)
            # Append source1 and source2 to ALU_in as elements 2 and 3
            self.ALU_in.append(source1) 
            self.ALU_in.append(source2) 

        ###################################
        # Immediate Arithmetic Operations #
        ###################################
        elif (self.inst_op == "addi") or (self.inst_op == "subi"):
            '''
            Immediate Arithmetic Operation Structure
            |--------------------------------|
            |  OP  , dest , src1 | immediate |
            | addi ,  $1  ,  $2  |  #34233   |
            |--------------------------------|
            |  OP  , dest , src1 | immediate |
            | subi ,  $1  ,  $2  |  #34233   |
            |--------------------------------|
            '''
            # Decode Destination Field
            destination = int(self.decodeField1().split("$")[1])

            # Decode Source 1 Field
            source1 = int(self.decodeSource1Field().split("$")[1])

            # Decode Immediate
            immediate = int(self.decodeImmediateValue().split("#")[1])

            print(self.inst_op,destination,source1,immediate)

            # Append destination register to ALU_in as element 1
            self.ALU_in.append(destination)
            # Append source1 to ALU_in as element 2
            self.ALU_in.append(source1)
            # Append immediate to ALU_in as element 3
            self.ALU_in.append(immediate)

            

        ######################
        # logical Operations #
        ######################
        elif (self.inst_op == "and") or (self.inst_op == "or") or (self.inst_op == "not") or (self.inst_op == "nand") or (self.inst_op == "nor"):
            '''
            Logical Operation Structure
            |---------------------------|
            | OP   , dest , src1 , src2 |
            | and  ,  $1  ,  $2  ,  $3  |
            | or   ,  $1  ,  $2  ,  $3  |
            | not  ,  $1  ,  $2  ,  $3  |
            | nand ,  $1  ,  $2  ,  $3  |
            | nor  ,  $1  ,  $2  ,  $3  |
            |---------------------------|
            '''
            


        #####################
        # Branch Operations #
        #####################
        elif (self.inst_op == "beq") or (self.inst_op == "bne") or (self.inst_op == "bez") or (self.inst_op == "bnz") or (self.inst_op == "bgt") or (self.inst_op == "blt") or (self.inst_op == "bge") or (self.inst_op == "ble"):
            '''
            Branch Operation Structure
            |---------------------------|
            | OP  , src1 , src2 , LABEL |
            | beq ,  $1  ,  $2  , Loop  |
            | bne ,  $1  ,  $2  , Loop  |
            | bgt ,  $1  ,  $2  , Loop  |
            | blt ,  $1  ,  $2  , Loop  |
            | bge ,  $1  ,  $2  , Loop  |
            | ble ,  $1  ,  $2  , Loop  |
            |---------------------------|
            | OP  , src1 ,     LABEL    |
            | bez ,  $1  ,     Loop     | 
            |---------------------------|
            '''
            if (self.inst_op == "bez") or (self.inst_op == "bnz"):
                # Decode Source 1 Field
                source1 = int(self.decodeField1().split("$")[1])

                # fetch register value and convert to int
                value1 = int(self.data_reg[source1].read(), 2)

                # Compare value to zero
                if (self.inst_op == "bez"):
                    if value1 == 0:
                        print("true! value == 0")
                    else:
                        print("false! value != 0")
                if (self.inst_op == "bnz"):
                    if not value1 == 0:
                        print("true! value != 0")
                    else:
                        print("false! value == 0")
            else:
                # Decode Source 1 Field
                source1 = self.decodeField1()

                # Decode Source 2 Field
                source2 = self.decodeSource1Field()


                # split source into index and source register address
                source1 = source1.split("$")[1]
                source2 = source2.split("$")[1]

                # Decode label??

                # fetch register value and convert to int
                print("source1 address",source1)
                print("source2 address",source2)
                value1 = int(self.data_reg[int(source1)].read(), 2)
                value2 = int(self.data_reg[int(source2)].read(), 2)

                if (self.inst_op == "beq"):
                    if value1 == value2:
                        print("true! value1 == value2")
                    else:
                        print("false! value1 != value2")
                elif (self.inst_op == "bne"):
                    if not value1 == value2:
                        print("true! value1 != value2")
                    else:
                        print("false! value1 == value2")
                elif (self.inst_op == "bgt"):
                    if value1 > value2:
                        print("true! value1 > value2")
                    else:
                        print("false! value1 < value2")
                elif (self.inst_op == "blt"):
                    if value1 < value2:
                        print("true! value1 < value2")
                    else:
                        print("false! value1 > value2")
                elif (self.inst_op == "bge"):
                    if value1 >= value2:
                        print("true! value1 >= value2")
                    else:
                        print("false! value1 <= value2")
                elif (self.inst_op == "ble"):
                    if value1 <= value2:
                        print("true! value1 <= value2")
                    else:
                        print("false! value1 >= value2")


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
        self.inst_immediate_bin = self.instruction[15:32]
        #print("Length:",len(str(self.inst_immediate_bin)))
        #print("Instruction Immediate Binary:",self.inst_immediate_bin)
        
        # Error check to confirm that destination field does not contain a register that does not exist(>32)
        if int(self.inst_immediate_bin, 2) > 131071:
            print("Cannot use numbers large than 131071")
            sys.exit(4)

        # Convert the extracted binary to a register number
        self.inst_immediate = "#" + str(int(self.inst_immediate_bin))
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
        
        self.checkIfStallNeeded()
        return self.inst


    def checkIfStallNeeded(self):
        
        
        if ((self.inst_source1 or self.inst_source2) == self.WB_addr):
            self.need_stall = True



