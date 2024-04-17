#Assembler made in python
# write functions for all types here
from dict import *
def sext_s(n):
    """
    sgn-extend a 12-bit integer to a 12-bit binary string.
    >>> sextS(10)
    '000000001010' uses left shifting
    """
    bs = bin(n & ((1 << 12) - 1))[2:].zfill(12)
    return bs
def sext_i(n):
   bs = bin(n & ((1 << 12) - 1))[2:].zfill(12)
   return bs

def sext_j(n):
    bs = bin(n & ((1 << 21) - 1))[2:].zfill(21)
    return bs

def sext_u(n):
    bs = bin(n & ((1 << 32) - 1))[2:].zfill(32)
    return bs[:20:]

def sext_b(n):
    bs = bin(n & ((1 << 13) - 1))[2:].zfill(13)
    return bs
   
def s_type(instruction,regi_dict):
    register = instruction[1:len(instruction):1]
    register[1],reg=register[1].split('(')
    reg=reg[0:-1:1]
    register.append(reg)
    t=sext_s(int(register[1]))
    return t[0:7]+regi_dict[register[0]]+regi_dict[register[2]]+"010"+t[7:12]+"0100011"

def r_type(regi_dict,function3_r,function7_r,instruction,r_instruct):
    return function7_r[instruction[0]]+regi_dict[instruction[3]]+regi_dict[instruction[2]]+function3_r[instruction[0]]+regi_dict[instruction[1]]+r_instruct[instruction[0]]
def u_type(instruction,regi_dict,u_instruct):
    opcode=u_instruct[instruction[0]]
    t=sext_u(int(instruction[2]))
    return t+regi_dict[instruction[1]]+opcode

def i_type(instruction, regi_dict,function3_i,i_instruct):


    if instruction[0] == "lw":
        instruction[2], reg = instruction[2].split('(')
        reg=reg[0:-1:]
        
        imm = sext_i(int(instruction[2]))
        return imm+ regi_dict[reg] + function3_i[instruction[0]] +regi_dict[instruction[1]]+i_instruct[instruction[0]]

    imm= sext_i(int(instruction[3]))
    return imm+ regi_dict[instruction[2]] + function3_i[instruction[0]] + regi_dict[instruction[1]]+i_instruct[instruction[0]]

def j_type(instruction, counter, labelAdd):
    if instruction[2] not in labelAdd:
        imm=sext_j(int(instruction[2]))
        return imm[0] + imm[10:20] + imm[-11] + imm[1:9] + regi_dict[instruction[1]] + "1101111"
    else:
        imm=sext_j(-4 * (counter - labelAdd[instruction[2]]))
        return imm[0] + imm[10:20] + imm[-11] + imm[1:9] + regi_dict[instruction[1]] + "1101111"



def b_type(instruction, counter, labelAdd):
    if instruction[3] not in labelAdd: 
        imm= sext_b(int(instruction[3]))
        return imm[0] + imm[2:8] + regi_dict[instruction[2]] + regi_dict[instruction[1]] + func3_b[instruction[0]] + imm[8:12] + imm[1] + b_instruct[instruction[0]]
    else:
        imm = sext_b(-(counter-labelAdd[instruction[3]])*4)
        return imm[0] + imm[2:8] + regi_dict[instruction[2]] + regi_dict[instruction[1]] + func3_b[instruction[0]] + imm[8:12] + imm[1] + b_instruct[instruction[0]]

