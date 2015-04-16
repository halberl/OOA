# Import sys for passing arguments
import sys
# Import re for splitting final instruction into chunks
import re

# Import instruction dictionary for instruction lookups
from instruction_dictionary import inst_dict
#For reading source code file and turning into
#executable instructions.
#NEEDS TO FLAG HAZARDS


# Get arguments
import sys
if len(sys.argv) > 1:
    print("argument",sys.argv[1])
else:
    print("No arguments Supplied")
    sys.exit(1)

# 1 read file line by line.  
instruction=sys.argv[1]
#instruction="ble,R31,R04";
# Split instruction by "," and store in inst_fields
inst_fields = instruction.split(',')

#for x in range(len(instruction)):
#	print("shit",x,instruction[x])
#	inst_fields[x] = instruction[x]

# Print each instruction field
print("inst_fields:")
print(inst_fields)

# Extract Instruction Operator from field 0
inst_op = inst_fields[0]

# Check if 4th character of Operator specifies immediate value
if inst_op[len(inst_op)-1] == "i":
    immediate_operation = 1
else:
    immediate_operation = 0

# Lookup Instruction Operator in dictionary
inst_op_bin = inst_dict[inst_fields[0]]
print("inst_op:", inst_op)
print("inst_op_bin:", inst_op_bin)


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






