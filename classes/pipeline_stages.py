import sys
import re
import json
# Import instruction dictionary for instruction lookups
#from dictionaries.instruction_dictionary import inst_dict
#from instruction_dictionary import inst_dict, blah1, blah2

# Read and Open dictionary python
#inst_dict = json.loads(open("dictionaries/dict2.py").read())



#For reading source code file and turning into
#executable instructions.
#NEEDS TO FLAG HAZARDS


# Create classes for functions
class DECODEFunction(object):
    '''
    This class is used to decode instructions passed to it. The instruction dictionary
    contains all specific bit mappings for each instruction operand. 
    '''
    # Read and Open dictionary file relative to root of project
    inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())

    def __init__(self, instruction):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        self.instruction = instruction
        print("Instruction:",self.instruction)
        #return self.instruction


    def splitFields(self):
        '''
        This constructor splits the instruction string into usable fields.
        '''
        # Split instruction by "," and store in inst_fields
        self.inst_fields = self.instruction.split(',')
        print("Instruction Fields:",self.inst_fields)
        #return self.inst_fields


    def decodeOpField(self):
        '''
        This constructor decodes the OP field of the instruction.
        '''

        # Extract Instruction Operator from field 0
        self.inst_op = self.inst_fields[0]
        print("Instruction OP:",self.inst_op)

        # Check if 4th character of Operator specifies immediate value
        if self.inst_op[len(self.inst_op)-1] == "i":
            immediate = 1
        else:
            immediate = 0
        print("Immediate?:",immediate)
