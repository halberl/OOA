from hw import register


class pipeline:
    def __init__(self, stack_ptr, inst_reg, data_reg, data_mem, inst_mem):
        # Initialize all variables
        self.stack_ptr = stack_ptr
        self.inst_reg = inst_reg
        self.data_reg = data_reg
        self.data_mem = data_mem
        self.inst_mem = inst_mem

        print(self.stack_ptr)
        print(self.inst_reg)
        print(self.data_reg)
        print(self.data_mem)
        print(self.inst_mem)


