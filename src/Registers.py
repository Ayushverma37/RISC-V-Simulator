import numpy as np

class Registers:
    def __init__(self):
        self.IR=0 # instruction register, holds the instruction to be executed
        # self.PC=0 # program counter, holds pointer to memory location containing instruction
        self.reg=np.zeros(32) # 32 general purpose registers
        self.reg[2]=0x7ffffff0 # stack pointer sp
        self.reg[3]=0x10000000 # global pointer gp
        self.reg[4]=0x00000000 # thread pointer tp
        self.reg[5]=0x00000000 # frame pointer fp
    
    def ReadIR(self):
        IRval=self.IR
        return IRval
    
    def WriteIR(self, WriteVal, writeIR):
        if(writeIR==True):
            self.IR=WriteVal

    def ReadPC(self):
        PCval=self.PC
        return PCval

    def WritePC(self, WriteVal, writePC):
        if(writePC==True):
            self.PC=WriteVal

    def WriteGpRegisters(self, RegNumber, RegWrite, WriteVal):
        if(RegNumber<0 or RegNumber>31):
            raise Exception("Invalid register number!")
        elif(RegNumber==0 or RegWrite==False):
            return 0
        # elif(RegWrite==0):
        #     raise Exception("RegWrite not activated! Cannot write to register")
        elif(WriteVal>=2**31 or WriteVal<-2**31):
            raise Exception("WriteValue out of range!")
        self.reg[RegNumber]=WriteVal
        print(f"Written {WriteVal} in x{RegNumber}")

    def ReadGpRegisters(self, RegNumber):
        if(RegNumber<0 or RegNumber>31):
            raise Exception("Invalid register number!")
        # elif(RegRead==0):
        #     raise Exception("RegRead not activated! Cannot read register")
        elif(RegNumber==0):
            return 0
        val=self.reg[RegNumber]
        print(f"Read {val} from x{RegNumber}")
        return val
