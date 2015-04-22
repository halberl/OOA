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

        #print("Instruction:",self.instruction)




    def executeOperation(self):
                
        # map the inputs to the function blocks
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



    def ld(self):
        print("In the ld constructor")
        print(self.operation + self.destination + self.source1 + self.source2)
    def st(self):
        print("In the ld constructor")
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
#    def sub(self):
#    def mul(self):
#    def div(self):
#    def addi(self):
#    def subi(self):
#    def muli(self):
#    def divi(self):
#    def and(self):
#    def or(self):
#    def not(self):
#    def nand(self):
#    def nor(self):
#    def beq(self):
#    def bne(self):
#    def bez(self):
#    def bnz(self):
#    def bgt(self):
#    def blt(self):
#    def bge(self):
#    def ble(self):
