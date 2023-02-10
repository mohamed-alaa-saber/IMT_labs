def setbit(reg,bit):
    bit=int(bit) #input validation
    reg |= (1<<bit)
    return reg
def clrbit(reg,bit):
    bit=int(bit) #input validation
    reg &= ~(1<<bit)
    return reg
def togbit(reg,bit):
    bit=int(bit) #input validation
    reg ^= (1<<bit)
    return reg
def getbit(reg,bit):
    bit=int(bit) #input validation
    return ((reg>>bit)&1)





x=0x08

x=setbit(x,2)
print(x)
x=clrbit(x,2)
print(x)
x=togbit(x,1)
print(x)
x=getbit(x,3)
print(x)