class RingBuffer:
    def __init__(self,sizemax):
        self.data = [None for i in range(sizemax)]
        self.sizemax = sizemax
        self.leftspace = sizemax
        self.currWrite = 0
        self.currRead = 0
    def read(self,):
        length = self.data[self.currRead]
        self.currRead += 1

        res = [ val for val in self.data[self.currRead:self.currRead+1]]
        self.currRead += length
        self.updatePosition()

    def write(self,x):
        # suppose x is a list type
        currlen = len(x)
        # check whether could write
        # tmp = self.currWrite
        # for i in range(currlen):
        #     self.currWrite += 1
        #     if self.updatePosition():
        #         continue
        #     else:
        #         return "Full"
        
        # now able to write
        self.currWrite  = tmp
            self.data[self.currWrite] = len(x)
            for i in x:
                self.data[self.currWrite] = i
                self.currWrite+=1
                # problem 

    def updatePosition(self):
        if self.currRead > self.sizemax:
            self.currRead = self.currRead % self.sizemax
        if  self.currWrite > self.sizemax:
            self.currWrite = self.currWrite % self.sizemax
        if self.currWrite == self.currRead:
            return False
        else:
            return True 
    
        
        
