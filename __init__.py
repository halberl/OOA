from hw import register
from hw import mem_collection

NUM_OF_REG=32
SIZE_OF_INST_MEM=2048
SIZE_OF_DATA_MEM=32768

if __name__ == "__main__":
    #create registers
    data_reg=[]

    for it in range (0,NUM_OF_REG):
        name="r{0}".format(it)
        data_reg.append(register(name))

    #for ti in range(len(data_reg)):
        #print "Index = {0}".format(ti)
        #print data_reg[ti].get_name()
        #print ti
        
    #create memory
    inst_mem=mem_collection("inst", SIZE_OF_INST_MEM)
    data_mem=mem_collection("data", SIZE_OF_DATA_MEM)


    print "Done initializing mem and reg"
