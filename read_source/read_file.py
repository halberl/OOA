import binascii
from instruction_dictionary import inst_dict
#For reading source code file and turning into
#executable instructions.
#NEEDS TO FLAG HAZARDS

# 1 read file line by line.  
instruction="move,#15,#04";
instruction = instruction.split(',');
instruction_destination = instruction[1].split('#')[1];
instruction_source = instruction[2].split('#')[1];


# 2 convert instructions into 32bit code
print "dictionary['", instruction[0], "']: ", inst_dict[instruction[0]];
OPCODE=inst_dict[instruction[0]];

# convert decimal to binary
print "inst_dest: ", instruction_destination;
destination = bin(int(instruction_destination)); 
print "destination: ", destination;  

print "inst_source: ", instruction_source;
source = bin(int(instruction_source)); 
print "source: ", source;  


# 3 check for hazards






