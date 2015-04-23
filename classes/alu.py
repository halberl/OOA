'''
Filename: alu.py
Author:   Lucas Halbert
Date:     4/22/15
Modified: 4/22/15
Description: Class declarations for different functions of the ALU (arithmetic logic unit) 
'''
import sys
import re
import json

#NEEDS TO FLAG HAZARDS

'''
Class declarations for the ALU
'''
class ALU(object):
    '''
    This class is used to perform arithmetic operations on instructions
    '''

    def __init__(self, operation, destination, source1, source2):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        # Read and Open dictionary file relative to root of project
        self.inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())

        # Initialize variables
        self.operation = operation
        self.destination = destination
        self.source1 = source1
        self.source2 = source2


    def executeOperation(self):
                
        # map the operators to the function blocks
        
        if self.operation == "ld":
            self.ld()
        elif self.operation == "st":
            self.st()
        elif self.operation == "move":
            self.move()
        elif self.operation == "swap":
            self.swap()
        elif self.operation == "add":
            self.add()
        elif self.operation == "sub":
            self.sub()
        elif self.operation == "mul":
            self.mul()
        elif self.operation == "div":
            self.div()
        elif self.operation == "addi":
            self.addi()
        elif self.operation == "subi":
            self.subi()
        elif self.operation == "muli":
            self.muli()
        elif self.operation == "divi":
            self.divi()
        elif self.operation == "and":
            self.and()
        elif self.operation == "or":
            self.or()
        elif self.operation == "not":
            self.not()
        elif self.operation == "nand":
            self.nand()
        elif self.operation == "nor":
            self.nor()
        elif self.operation == "beq":
            self.beq()
        elif self.operation == "bne":
            self.bne()
        elif self.operation == "bez":
            self.bez()
        elif self.operation == "bnz":
            self.bnz()
        elif self.operation == "bgt":
            self.bgt()
        elif self.operation == "blt":
            self.blt()
        elif self.operation == "bge":
            self.bge()
        elif self.operation == "ble":
            self.ble()




    def ld(self):
        print("In the ld constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def st(self):
        print("In the st constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def move(self):
        print("In the move constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def swap(self):
        print("In the swap constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def add(self):
        print("In the add constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def sub(self):
        print("In the sub constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def mul(self):
        print("In the mul constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def div(self):
        print("In the div constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def addi(self):
        print("In the addi constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def subi(self):
        print("In the subi constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def muli(self):
        print("In the muli constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def divi(self):
        print("In the divi constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def and(self):
        print("In the and constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def or(self):
        print("In the or constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def not(self):
        print("In the not constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def nand(self):
        print("In the nand constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def nor(self):
        print("In the nor constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def beq(self):
        print("In the beq constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def bne(self):
        print("In the bne constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def bez(self):
        print("In the bez constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def bnz(self):
        print("In the bnz constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def bgt(self):
        print("In the bgt constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def blt(self):
        print("In the blt constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def bge(self):
        print("In the bge constructor")
        print(self.operation + self.destination + self.source1 + self.source2)

    def ble(self):
        print("In the ble constructor")
        print(self.operation + self.destination + self.source1 + self.source2)
