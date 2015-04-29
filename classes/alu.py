'''
Filename: alu.py
Author:   Lucas Halbert
Date:     4/22/15
Modified: 4/29/15
Description: Class declarations for different functions of the ALU (arithmetic logic unit) 
'''
import sys
import re
import json
import hw

#NEEDS TO FLAG HAZARDS

'''
Class declarations for the ALU
'''
class ALU(object):
    '''
    This class is used to perform arithmetic operations on instructions
    '''

    def __init__(self, data_reg, ALU_in):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        # Read and Open dictionary file relative to root of project
        #self.inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())

        
        # Initialize variables
        self.data_reg = data_reg
        self.ALU_in = ALU_in
        self.ALU_out = []
        if self.ALU_in == None:
            return
        print("Self.ALU_in:",self.ALU_in)

        # Initialize/clear self.ALU_out before next instruction data

        self.executeOperation()

        # Clear self.ALU_in for new incoming data
        self.ALU_in = []

    def executeOperation(self):
        '''
        This constructor calls the operator constructor based on the OP filed of the instruction
        '''
                
        if self.ALU_in == None:
            self.stall = True
            self.noop()
        elif self.ALU_in[0] == "ld":
            self.ld()
        elif self.ALU_in[0] == "st":
            self.st()
        elif self.ALU_in[0] == "move":
            self.move()
        elif self.ALU_in[0] == "swap":
            self.swap()
        elif self.ALU_in[0] == "add":
            self.add()
        elif self.ALU_in[0] == "sub":
            self.sub()
        elif self.ALU_in[0] == "mul":
            self.mul()
        elif self.ALU_in[0] == "div":
            self.div()
        elif self.ALU_in[0] == "addi":
            self.addi()
        elif self.ALU_in[0] == "subi":
            self.subi()
        elif self.ALU_in[0] == "muli":
            self.muli()
        elif self.ALU_in[0] == "divi":
            self.divi()
        elif self.ALU_in[0] == "and":
            self.and1()
        elif self.ALU_in[0] == "or":
            self.or1()
        elif self.ALU_in[0] == "not":
            self.not1()
        elif self.ALU_in[0] == "nand":
            self.nand()
        elif self.ALU_in[0] == "nor":
            self.nor()
        elif self.ALU_in[0] == "beq":
            self.beq()
        elif self.ALU_in[0] == "bne":
            self.bne()
        elif self.ALU_in[0] == "bez":
            self.bez()
        elif self.ALU_in[0] == "bnz":
            self.bnz()
        elif self.ALU_in[0] == "bgt":
            self.bgt()
        elif self.ALU_in[0] == "blt":
            self.blt()
        elif self.ALU_in[0] == "bge":
            self.bge()
        elif self.ALU_in[0] == "ble":
            self.ble()


    def noop(self):
        print("In the noop constructor")
        self.ALU_out = self.ALU_in

    def ld(self):
        print("In the ld constructor")
        
        # Pass mem operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def st(self):
        print("In the st constructor")
        
        # Pass mem operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def move(self):
        print("In the move constructor")
        
        # Pass mem operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def swap(self):
        print("In the swap constructor")
        
        # Pass mem operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def add(self):
        print("In the add constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        # Append register destination to ALU_out
        self.ALU_out.append(int(self.data_reg[self.ALU_in[1]].read(), 2))

        # Perform arithmatic
        self.ALU_out.append(int(self.data_reg[self.ALU_in[2]].read(), 2) + int(self.data_reg[self.ALU_in[3]].read(), 2))
        print(self.ALU_out)

    def sub(self):
        print("In the sub constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        # Append register destination to ALU_out
        self.ALU_out.append(int(self.data_reg[self.ALU_in[1]].read(), 2))

        # Perform arithmatic
        self.ALU_out.append(int(self.data_reg[self.ALU_in[2]].read(), 2) - int(self.data_reg[self.ALU_in[3]].read(), 2))
        print(self.ALU_out)

    def mul(self):
        print("In the mul constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        # Append register destination to ALU_out
        self.ALU_out.append(int(self.data_reg[self.ALU_in[1]].read(), 2))

        # Perform arithmatic
        self.ALU_out.append(int(self.data_reg[self.ALU_in[2]].read(), 2) * int(self.data_reg[self.ALU_in[3]].read(), 2))
        print(self.ALU_out)

    def div(self):
        print("In the div constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        # Append register destination to ALU_out
        self.ALU_out.append(int(self.data_reg[self.ALU_in[1]].read(), 2))

        # Perform arithmatic
        self.ALU_out.append(int(self.data_reg[self.ALU_in[2]].read(), 2) / int(self.data_reg[self.ALU_in[3]].read(), 2))
        print(self.ALU_out)

    def addi(self):
        print("In the addi constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        # Append register destination to ALU_out
        self.ALU_out.append(int(self.data_reg[self.ALU_in[1]].read(), 2))

        # Perform arithmatic
        self.ALU_out.append(int(self.data_reg[self.ALU_in[2]].read(), 2) + int(self.ALU_in[3]))
        print(self.ALU_out)

    def subi(self):
        print("In the subi constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        self.ALU_out.append(int(self.data_reg[self.ALU_in[1]].read(), 2))

        # Perform arithmatic
        self.ALU_out.append(int(self.data_reg[self.ALU_in[2]].read(), 2) - int(self.ALU_in[3]))
        print(self.ALU_out)

    def and1(self):
        print("In the and constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        print(self.operation + self.destination + self.source1 + self.source2)

    def or1(self):
        print("In the or constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        print(self.operation + self.destination + self.source1 + self.source2)

    def not1(self):
        print("In the not constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        print(self.operation + self.destination + self.source1 + self.source2)

    def nand(self):
        print("In the nand constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        print(self.operation + self.destination + self.source1 + self.source2)

    def nor(self):
        print("In the nor constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])

        print(self.operation + self.destination + self.source1 + self.source2)

    def beq(self):
        print("In the beq constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def bne(self):
        print("In the bne constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def bez(self):
        print("In the bez constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def bnz(self):
        print("In the bnz constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def bgt(self):
        print("In the bgt constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def blt(self):
        print("In the blt constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def bge(self):
        print("In the bge constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)

    def ble(self):
        print("In the ble constructor")

        # Append instruction operation to ALU_out
        self.ALU_out.append(self.ALU_in[0])


        # Pass branch operation to MEM stage
        self.ALU_out = self.ALU_in
        print(self.ALU_out)
