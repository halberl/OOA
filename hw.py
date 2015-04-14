# Define all the hardware classes

#32-bit strings for initializing and testing
ALL_ZEROS="00000000000000000000000000000000"
ALT_FROM_1="10101010101010101010101010101010"
ALT_FROM_0="01010101010101010101010101010101"

class register:
    data="0"*32
    def __init__(self, name):
        self.name = name

    def write(self, data):
        self.data=data

    def read(self):
        return self.data

    def get_name(self):
        return self.name

class mem_collection:
    def __init__(self, name, size):
        self.name=name
        self.mem = [ALL_ZEROS]*size
        #for index in range(size):
            #self.mem[index]=ALL_ZEROS

    def load(self, addr):
        return self.mem[addr]

    def save(self, addr, value):
        self.mem[addr]=value
