from hw import register
from hw import mem_collection
from assemblyfile2bin import FileToBin
import sys

NUM_OF_REG=32
SIZE_OF_INST_MEM=2048
SIZE_OF_DATA_MEM=32768

# Pull source file from command line arguments
SOURCE_FILE = sys.argv[1]
if SOURCE_FILE == "":
    SOURCE_FILE = "assemblySource.txt"
BIN_FILE = "binFile.txt"

def main():
    #create registers
    data_reg=[]

    for it in range (0,NUM_OF_REG):
        name="r{0}".format(it)
        data_reg.append(register(name))
        
    #create memory
    inst_mem=mem_collection("inst", SIZE_OF_INST_MEM)
    data_mem=mem_collection("data", SIZE_OF_DATA_MEM)

    print("Done initializing mem and reg")

    print("Read assembly file and convert to binary")

    f = FileToBin(SOURCE_FILE, BIN_FILE)
    print("Called FileToBin")
    f.read()
    print("Read source file")
    f.write()

    print("Done converting to assembly.  Next send to instruction memory")


if __name__ == "__main__":
    main()
