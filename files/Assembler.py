#Assembler made in python
# write functions for all types here
def sextRISB(n):
   binary_string = bin(n & ((1 << 12) - 1))[2:].zfill(12)
   return binary_string

def sextJ(n):
    binary_string = bin(n & ((1 << 21) - 1))[2:].zfill(21)
    return binary_string

def sextU(n):
    binary_string = bin(n & ((1 << 20) - 1))[2:].zfill(20)
    return binary_string

def sextB(n):
    binary_string = bin(n & ((1 << 13) - 1))[2:].zfill(13)
    return binary_string

def r_type(regi_dict,function3_r,function7_r,instruction,r_instruct):
    return function7_r[instruction[0]]+regi_dict[instruction[3]]+regi_dict[instruction[2]]+function3_r[instruction[0]]+regi_dict[instruction[1]]+r_instruct[instruction[0]]
def utype(instruction,regi_dict,u_instruct):
    opcode=u_instruct[instruction[0]]
    t=sextU(int(instruction[2]))
    return t+regi_dict[instruction[1]+opcode
