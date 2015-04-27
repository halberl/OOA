# Define all the hardware classes

#32-bit strings for initializing and testing
ALL_ZEROS="00000000000000000000000000000000"
ALT_FROM_1="10101010101010101010101010101010"
ALT_FROM_0="01010101010101010101010101010101"

class register:
    def __init__(self):
        self.data = ALL_ZEROS

    def write(self, data):
        self.data=data

    def read(self):
        return self.data


class mem_collection:
    def __init__(self, name, size):
        self.name=name
        self.mem = [ALL_ZEROS]*size
        #for index in range(size):
            #self.mem[index]=ALL_ZEROS


    def save_all(self, arr):
        '''
        save all binary from instruction binary array into the memory
        '''
        for it in range (0, len(arr)):
            self.save(it, arr[it])

    def load(self, addr):
        return self.mem[addr]

    def save(self, addr, value):
        self.mem[addr]=value
