from hw import register
from classes.decode import INSTRUCTIONDecode
from classes.alu import ALU


class pipeline:
    '''
    This class sets up pipeline variables and controls the pipeline stages
    '''
    def __init__(self, stack_ptr, inst_reg, data_reg, data_mem, inst_mem):
        '''
        This Constructor initializes all pipeline variables
        '''
        # Initialize all variables
        self.stack_ptr = stack_ptr
        self.inst_reg = inst_reg
        self.data_reg = data_reg
        self.data_mem = data_mem
        self.inst_mem = inst_mem

        '''
        print(self.stack_ptr.read())
        print("Inst_reg: ", self.inst_reg.read())
        print(self.data_reg[3].read())
        print(self.data_mem.load(3))
        print(self.inst_mem.load(3))
        '''
        self.start_pipeline()


    def start_pipeline(self):
        '''
        This Constructor starts the pipeline, and increments the stack_ptr to keep track of instruction execution
        '''
        while(self.inst_mem.load(int(self.stack_ptr.read(), 2)).rjust(32, '0') != "0".rjust(32, '0')):
            #print("Compare: ",self.inst_mem.load(int(self.stack_ptr.read(), 2)).rjust(32, '0'), "to", "0".rjust(32, '0'))

            # Place inst_mem[stack_ptr] into inst_reg
            #print("\n\nSTART LOADING MEMORY WITH STUFF")
    
            # convert stack pointer binary to an a string(decimal)
            #print("Stack ptr: ", str(int(self.stack_ptr.read(), 2)))

            # Display inst_mem[stack_ptr]
            #print("inst_mem[",int(self.stack_ptr.read(), 2),"]: ", self.inst_mem.load(int(self.stack_ptr.read(), 2)))

            '''
            self.fetch() does this now
            # Write inst_mem[stack_ptr] to inst_reg
            self.inst_reg.write(int(self.inst_mem.load(int(self.stack_ptr.read(), 2))))

            # Read inst_reg
            print("inst_reg: ", self.inst_reg.read())
            '''

            ###
            # Initial values should be some sort of NULL.  If null, do nothing and return
            ###

            # Start instruction result write back
            self.writeBack()

            # Start instruction memory operations
            self.memory()

            # Start instruction execution
            self.execute()

            # Start instruction decode
            self.decode()

            # Start instruction fetch
            self.fetch()


            # Print New lines to seperate instructions
            print("\n\n\n")


            '''
            # convert stack_ptr to int, increment stack ptr, and convert back to padded str
            temp_stack_ptr = "{0:b}".format(int(str(int(self.stack_ptr.read(), 2) + 1))).rjust(32, '0')

            # Set new stack_ptr
            self.stack_ptr.write(str(temp_stack_ptr).rjust(32, '0'))
            '''

            



    def fetch(self):
        '''
        Fetch current instruction from the instruction memory and place in the instruction register
        '''
        print("\n|----------------------|")
        print("| Entering fetch stage |")
        print("|----------------------|")
        # Write inst_mem[stack_ptr] to inst_reg
        self.inst_reg.write(int(self.inst_mem.load(int(self.stack_ptr.read(), 2))))

        # print stack_ptr
        print("Stack_ptr: ",int(self.stack_ptr.read(), 2))
        # Read inst_reg
        print("inst_reg: ", self.inst_reg.read())


        
        # convert stack_ptr to int, increment stack ptr, and convert back to padded str
        temp_stack_ptr = "{0:b}".format(int(str(int(self.stack_ptr.read(), 2) + 1))).rjust(32, '0')

        # Set new stack_ptr
        self.stack_ptr.write(str(temp_stack_ptr).rjust(32, '0'))
        


    def decode(self):
        '''
        Decode instruction in the instruction register
        '''
        print("\n|-----------------------|")
        print("| Entering decode stage |")
        print("|-----------------------|")
        a=INSTRUCTIONDecode(self.inst_reg.read())
        self.op = a.decodeOpField()
        self.dest = a.decodeDestField()
        self.source1 = a.decodeSource1Field()
        self.source2 = a.decodeSource2Field()
        self.immediate = a.decodeImmediateValue()
        a.constructInstruction()

    def execute(self):
        '''
        Do ALU operation specified in the instruction
        '''
        print("\n|------------------------|")
        print("| Entering execute stage |")
        print("|------------------------|")

        #(self, operation, destination, source1, source2) 
        a=ALU(self.op, self.dest, self.source1, self.source2)
        a.executeOperation()

         

    def memory(self):
        '''
        Do memory operations
        '''
		# Read from or write to memory
        # Needs to know 
          # which operation to perform
          # what value to store if any
          # what location to store/read in memory

        if ( X ):
            #Read
            value_to_write = self.data_mem[mem_location]

        else if ( X ):
            #Write
            self.data_mem[mem_location] = value_to_store

        print("\n|-----------------------|")
        print("| Entering memory stage |")
        print("|-----------------------|")


    def writeBack(self):
        '''
        Do write back to registers 
        '''
        # Needs to know
          # what register to write in
          # what value to write
        #Arguments
        reg_number
        value_to_write

        #Operation
        self.data_reg[reg_number] = value_to_write



        print("\n|---------------------------|")
        print("| Entering write back stage |")
        print("|---------------------------|")

