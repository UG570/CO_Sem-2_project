#Assembler made in python
# write functions for all types here
from dict import *
from main import labelAdd
def sextS(n):
    """
    sgn-extend a 12-bit integer to a 12-bit binary string.
    >>> sextS(10)
    '000000001010' uses left shifting
    """
    binary_string = bin(n & ((1 << 12) - 1))[2:].zfill(12)
    return binary_string
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
   
def s_type(instruction,regi_dict):
    register = instruction[1:len(instruction):1]
    register[1],reg=register[1].split('(')
    reg=reg[0:-1:1]
    register.append(reg)
    t=sextS(int(register[1]))
    return t[0:7]+regi_dict[register[0]]+regi_dict[register[2]]+"010"+t[7:12]+"0100011"

def r_type(regi_dict,function3_r,function7_r,instruction,r_instruct):
    return function7_r[instruction[0]]+regi_dict[instruction[3]]+regi_dict[instruction[2]]+function3_r[instruction[0]]+regi_dict[instruction[1]]+r_instruct[instruction[0]]
def u_type(instruction,regi_dict,u_instruct):
    opcode=u_instruct[instruction[0]]
    t=sextU(int(instruction[2]))
    return t+regi_dict[instruction[1]]+opcode

def i_type(instruction, regi_dict,function3_i,i_instruct):


    if instruction[0] == "lw":
        instruction[2], temp = instruction[2].split('(')
        temp=temp[0:-1:]
        
        t = sextRISB(int(instruction[2]))
        return t + regi_dict[temp] + function3_i[instruction[0]] +regi_dict[instruction[1]]+i_instruct[instruction[0]]

    t = sextRISB(int(instruction[3]))
    return t + regi_dict[instruction[2]] + function3_i[instruction[0]] + regi_dict[instruction[1]]+i_instruct[instruction[0]]

    t = sextRISB(int(instruction[3]))
    return t + regi_dict[instruction[2]] + function3_i[instruction[0]] + regi_dict[instruction[1]]+i_instruct[instruction[0]]

def j_type(instruction):
    register = instruction[1::]
    t=sextJ(int(register[1]))
    return t[0]+t[9:20]+t[9]+t[1:8]+regi_dict[register[0]]+"0010111"



def b_type(instruction, counter):
    opcode = "1100011"
    if instruction[3] not in labelAdd: 
        t = sextB(int(instruction[3]))
        return t[0] + t[2:8] + regi_dict[instruction[2]] + regi_dict[instruction[1]] + b_instruct[instruction[0]] + t[8:12] + t[1] + opcode
    else:
        t = sextB((counter-labelAdd[instruction[3]])*4)
        return t[0] + t[2:8] + regi_dict[instruction[2]] + regi_dict[instruction[1]] + b_instruct[instruction[0]] + t[8:12] + t[1] + opcode

