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
    #inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())

    def __init__(self, instruction):
        '''
        This constructor initilizes the instruction variable and splits it into its proper
        fields based on the last character of the op portion. If an "i" is present, the 
        instruction is expecting field[3] to be an immediate value.
        '''
        #self.inst_dict = inst_dict
        # Read and Open dictionary file relative to root of project
        self.inst_dict = json.loads(open("dictionaries/instruction_dictionary.py").read())
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

        self.inst_op_bin = self.inst_dict[self.inst_fields[0]]
        print("Instruction OP:",self.inst_fields[0])
        print("Instruction OP Binary:",self.inst_op_bin)


    def decodeDestField(self):
        '''
        This constructor decodes the destination field of the instruction
        '''

        # Extract instruction destination from field 1
        self.inst_dest = self.inst_fields[1]
        print("Instruction Destination:",self.inst_dest)

        # Error check to confirm that field 1 does not contain a register that does not exist(>31)
        if int(self.inst_dest.split('$')[1]) > 31:
            print("Register",self.inst_dest,"does not exist")
            sys.exit(4)

        # Convert instruction destination to binary and pad to 5 bits MSB
        self.inst_dest_bin = "{0:b}".format(int(self.inst_fields[1].split('$')[1])).rjust(5, '0')
        print("Instruction Dest Binary:",self.inst_dest_bin)


'''
# Extract instruction destination from field 1
inst_dest = inst_fields[1]
if int(inst_dest.split('$')[1]) > 31:
    print("Register",inst_dest,"does not exist")
    sys.exit(4)
# Pad register location
inst_dest_bin = "{0:b}".format(int(inst_fields[1].split('$')[1])).rjust(5, '0')

## Check if the leading character is a $ or #
#if inst_dest.find("$") == 0:
#	# Destination is a register
#	#print("Destination is a register number")
#	inst_dest_bin = "{0:b}".format(int(inst_fields[1].split('$')[1])).rjust(5, '0')
#elif inst_dest.find("#") == 0:
#	# Destination is an immediate value
#	#print("Destination is an immediate value")
#	inst_dest_bin = "{0:b}".format(int(inst_fields[1].split('#')[1])).rjust(5, '0')
#else:
#	# Destination is corrupt
#	print("Destination is corrupt! Fail out!")
#	sys.exit(2)

# Print instruction destination
print("inst_dest:", inst_dest)
print("inst_dest_bin:", inst_dest_bin)



# Extract instruction source1 from field 2
inst_source1 = inst_fields[2]
# Pad register location
inst_source1_bin = "{0:b}".format(int(inst_fields[2].split('$')[1])).rjust(5, '0')

## Check if the leading character is a $ or #
#if inst_source1.find("$") == 0:
#        # Source1 is a register
#        inst_source1_bin = "{0:b}".format(int(inst_fields[2].split('$')[1])).rjust(5, '0')
#elif inst_source1.find("#") == 0:
#        # Source1 is an immediate value
#        inst_source1_bin = "{0:b}".format(int(inst_fields[2].split('#')[1])).rjust(5, '0')
#else:   
#        # Source1 is corrupt
#        print("Source1 is corrupt! Fail out!")
#        sys.exit(2)

# Print instruction source1
print("inst_source1:", inst_source1)
print("inst_source1_bin:", inst_source1_bin)




# Extract instruction source2 from field 3
inst_source2 = inst_fields[3]

# Check if the leading character is a $ or #
if inst_source2.find("$") == 0:
    # Source1 is a register
    inst_source2_bin = "{0:b}".format(int(inst_fields[3].split('$')[1])).rjust(5, '0')
elif inst_source2.find("#") == 0:
    # Source1 is an immediate value
    inst_source2_bin = "{0:b}".format(int(inst_fields[3].split('#')[1])).rjust(17, '0')
else:   
    # Source1 is corrupt
    print("Source2 is corrupt! Fail out!")
    sys.exit(2)
# Print instruction source2
print("inst_source2:", inst_source2)
print("inst_source2_bin:", inst_source2_bin)


# Combine OP, Dest, Source1, and Source2 into compiled binary
instruction_binary = inst_op_bin + inst_dest_bin + inst_source1_bin + inst_source2_bin
instruction_binary_len = len(instruction_binary)

# Force 32 bit length
instruction_binary = instruction_binary.ljust(32, '0')
print("Instruction Length:",len(instruction_binary))
print("Instruction Binary:",instruction_binary)



# Print formatted instruction and binary
print("|----------------------------------------------|")
if immediate_operation == 1:
    print("| OP    | DEST  | S1    | Immediate Val        |")
    print("|",inst_op_bin,"|",inst_dest_bin,"|",inst_source1_bin,"|",inst_source2_bin,"   |")
else:
    print("| OP    | DEST  | S1    | S2    | Unused       |")
    print("|",inst_op_bin,"|",inst_dest_bin,"|",inst_source1_bin,"|",inst_source2_bin,"|",32-instruction_binary_len,"bits      |")
#print("|",inst_op_bin,"|",inst_dest_bin,"|",inst_source1_bin,"|",inst_source2_bin,"|",32-instruction_binary_len,"bits     |")
#print("|",inst_op_bin,"|",inst_dest_bin,"|",inst_source1_bin,"|",inst_source2_bin,"| 00000000000 |")
print("|----------------------------------------------|")
#print(re.findall('.....', instruction_binary))

#inst_dest = int(inst_fields[1].split('$')[1]);
#instruction_source = int(instruction[2].split('$')[1]);


# 2 convert instructions into 32bit code
#print("dictionary['",instruction[0],"']: ", inst_dict[instruction[0]])
#OPCODE=inst_dict[instruction[0]];

# convert decimal to binary
#print("DECIMAL inst_dest: ", instruction_destination)
#destination = "{0:b}".format(instruction_destination).zfill(5)
#y = "{0:b}".format(instruction_destination).zfill(5)
#print y
#"{0:b}".format(31).zfill(5)
#print("destination: ", destination)

#print("DECIMAL inst_source: ", instruction_source)
#source = "{0:b}".format(instruction_source).zfill(5)
#print("source: ", source)


# 3 check for hazards
'''





