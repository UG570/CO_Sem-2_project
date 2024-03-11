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
