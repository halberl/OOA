from hw import register


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

            # Write inst_mem[stack_ptr] to inst_reg
            self.inst_reg.write(int(self.inst_mem.load(int(self.stack_ptr.read(), 2))))

            # Read inst_reg
            print("inst_reg: ", self.inst_reg.read())

            # convert stack_ptr to int, increment stack ptr, and convert back to padded str
            temp_stack_ptr = "{0:b}".format(int(str(int(self.stack_ptr.read(), 2) + 1))).rjust(32, '0')

            # Set new stack_ptr
            self.stack_ptr.write(str(temp_stack_ptr).rjust(32, '0'))

            

            # Next pass start IF stage


