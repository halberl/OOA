# Define all the hardware classes


class register:
    data="0"*32
    def __init__(self, name):
        self.name = name



# IDT this class is necessary
#class mem_addr:
#    data="0"*32
#    def __init__(self, addr):
#        self.addr=addr



class mem_collection:
    def __init__(self, name, size):
        self.name=name
        self.mem = []
        for index in range(size):
            mem[index]=mem_addr(index)

    def load(addr):
        return self.mem[addr]

    def save(addr, value):
        self.mem[addr]=value
