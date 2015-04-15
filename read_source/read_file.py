import binascii
from instruction_dictionary import inst_dict
#For reading source code file and turning into
#executable instructions.
#NEEDS TO FLAG HAZARDS

# 1 read file line by line.  
instruction="ble,R31,R04";
instruction = instruction.split(',');
instruction_destination = int(instruction[1].split('R')[1]);
instruction_source = int(instruction[2].split('R')[1]);


# 2 convert instructions into 32bit code
print "dictionary['",instruction[0],"']: ", inst_dict[instruction[0]];
OPCODE=inst_dict[instruction[0]];

# convert decimal to binary
print "DECIMAL inst_dest: ", instruction_destination
destination = "{0:b}".format(instruction_destination).zfill(5)
#y = "{0:b}".format(instruction_destination).zfill(5)
#print y
#"{0:b}".format(31).zfill(5)
print "destination: ", destination;  

print "DECIMAL inst_source: ", instruction_source;
source = "{0:b}".format(instruction_source).zfill(5)
print "source: ", source;  


# 3 check for hazards






