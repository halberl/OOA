from hw import register
from hw import mem_collection
from assemblyfile2bin import FileToBin
from pipeline import pipeline
import sys

NUM_OF_REG=31
SIZE_OF_INST_MEM=2048
SIZE_OF_DATA_MEM=32768

# Pull source file from command line arguments
SOURCE_FILE = sys.argv[1]
if SOURCE_FILE == "":
    SOURCE_FILE = "assemblySource.txt"
BIN_FILE = "binFile.txt"

def main():
    # Create Stack Pointer
    stack_ptr=register()

    # Create Instruction Register
    inst_reg=register()

    
    # Create registers
    data_reg=[]
    for it in range (0,NUM_OF_REG):
        data_reg.append(register())
        
    #create memory
    inst_mem=mem_collection("inst", SIZE_OF_INST_MEM)
    data_mem=mem_collection("data", SIZE_OF_DATA_MEM)
    print("Done initializing mem and reg")

    # All data Registers 
    print("\nData Registers")
    for it in range (0,NUM_OF_REG):
        print(data_reg[it].read())

    # Instruction Mem
    print("\nInstruction Memory")
    print(inst_mem.load(2))

    # Data Mem
    print("\nData Memory")
    print(data_mem.load(2))


    print("\n\nRead assembly file and convert to binary")
    f = FileToBin(SOURCE_FILE, BIN_FILE)


    # Read source file
    f.read()
    
    # write binary to bin file and return binary
    inst_binary_array = f.write()

    # print entire inst_binary_array
    print(inst_binary_array)

    # store all encoded binary to instruction memory
    inst_mem.save_all(inst_binary_array)

    


    '''
    Pipeline Starts here
    '''
    pipeline(stack_ptr, inst_reg, data_reg, data_mem, inst_mem)

    # print element 2 of instruction memory
    print(inst_mem.load(1))


    # Done??
    print("Done converting to assembly.  Next send to instruction memory")


if __name__ == "__main__":
    main()
