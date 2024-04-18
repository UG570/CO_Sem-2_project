import sys

register_index = {'00000': 0, '00001': 1, '00010': 2, '00011': 3, '00100': 4, '00101': 5, '00110': 6,
                    '00111': 7, '01000': 8, '01001': 9, '01010': 10, '01011': 11, '01100': 12, '01101': 13,
                    '01110': 14, '01111': 15, '10000': 16, '10001': 17, '10010': 18, '10011': 19, '10100': 20,
                    '10101': 21, '10110': 22, '10111': 23, '11000': 24, '11001': 25, '11010': 26, '11011': 27,
                    '11100': 28, '11101': 29, '11110': 30, '11111': 31}
register_values = [0]*32

mem = {'0x00010000': 0, '0x00010004': 0, '0x00010008': 0, '0x0001000c': 0, '0x00010010': 0,
        '0x00010014': 0, '0x00010018': 0, '0x0001001c': 0, '0x00010020': 0, '0x00010024': 0,
        '0x00010028': 0, '0x0001002c': 0, '0x00010030': 0, '0x00010034': 0, '0x00010038': 0,
        '0x0001003c': 0, '0x00010040': 0, '0x00010044': 0, '0x00010048': 0, '0x0001004c': 0,
        '0x00010050': 0, '0x00010054': 0, '0x00010058': 0, '0x0001005c': 0, '0x00010060': 0,
        '0x00010064': 0, '0x00010068': 0, '0x0001006c': 0, '0x00010070': 0, '0x00010074': 0,
        '0x00010078': 0, '0x0001007c': 0}
def unsigned(num):
    return ((num + 2**32) & 0b11111111111111111111111111111111)

def binaryToDec(string):
    dec = int(string, 2)
    if string[0] == '1':
        dec -= 1 << len(string)
    return dec

def twosComp32(n):
    return bin(unsigned(n))[2::].zfill(32)
    
def r_type_splitting(str):
    # global instruction
    if str[-15:-12:1]== "000":
        if str[0:7]== "0000000":
            instruction="add"
        else:
            instruction = "sub"
    elif str[-15:-12:1]== "001":
        instruction = "sll"
    elif str[-15:-12:1]== "010":
        instruction = "slt"
    elif str[-15:-12:1]== "011":
        instruction = "sltu"
    elif str[-15:-12:1]== "100":
        instruction = "xor"
    elif str[-15:-12:1]== "101":
        instruction = "srl"
    elif str[-15:-12:1]== "110":
        instruction = "or"
    elif str[-15:-12:1]== "111":
        instruction = "and"
    r_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])


def i_type_splitting(str):
    # global instruction
    if str[-15:-12:1]== "000":
        if str[0:7]== "0010011":
            instruction="addi"
        else:
            instruction = "jalr"
    elif str[-15:-12:1]== "010":
        instruction = "lw"
    elif str[-15:-12:1]== "011":
        instruction = "sltiu"
    i_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-32:-20])


def s_type_splitting(str):
    # global instruction
    if str[-15:-12:1]== "010":
            instruction="sw"
    s_type_implementation(instruction , str[::-25] + str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])


def b_type_splitting(str):
    # global instruction
    if str[-15:-12:1]== "000":
            instruction="beq"
    elif str[-15:-12:1]== "001":
        instruction = "bne"
    elif str[-15:-12:1]== "100":
        instruction = "blt"
    elif str[-15:-12:1]== "101":
        instruction = "bge"
    elif str[-15:-12:1]== "110":
        instruction = "bltu"
    elif str[-15:-12:1]== "111":
        instruction = "bgeu"
    b_type_implementation(instruction ,str[-12]+str[-11:-5], str[-20:-15:1], str[-25:-20:1])


def u_type_splitting(str):
    if str[0:7]=="0110111":
        instruction="lui"
    else:
        instruction="auipc"
    u_type_implementation(instruction ,str[-12:-7:1],str[-32:-12])


def j_type_splitting(str):
    if str[0:7]=="1101111":
        instruction="jal"
    j_type_implementation( instruction ,str[-21]+str[-11:-1]+str[-12]+str[-20:-12],str[-12:-7])


def r_type_implementation(instruction , rd, rs1, rs2):
    rd = register_index[rd]
    rs1 = register_index[rs1]
    rs2 = register_index[rs2]
    if instruction == "add":
        register_values[rd] = register_values[rs1] + register_values[rs2]
    elif instruction == "sub":
        register_values[rd] = register_values[rs1] - register_values[rs2]
    elif instruction == "sll":
        register_values[rd] = register_values[rs1] << int(bin(unsigned(register_values[rs2]))[-5::], 2)
    elif instruction == "slt":
        if(register_values[rs1] < register_values[rs2]):
            register_values[rd] = 1
    elif instruction == "sltu":
        if(unsigned(register_values[rs1]) < unsigned(register_values[rs2])):
            register_values[rd] = 1 
    elif instruction == "xor":
        register_values[rd] = register_values[rs1] ^ register_values[rs2]
    elif instruction == "srl":
        register_values[rd] = register_values[rs1] >> int(bin(unsigned(register_values[rs2]))[-5::], 2)
    elif instruction == "or":
        register_values[rd] = register_values[rs1] | register_values[rs2]
    elif instruction == "and":
        register_values[rd] = register_values[rs1] & register_values[rs2]

def s_type_implementation(instruction , imm, rs1, rs2):
    rs1 = register_index[rs1]
    imm = binaryToDec(imm)
    memory_address = "0x"+hex(register_values[rs1] + imm)[2::].zfill(8)
    mem[memory_address] = rs2



def u_type_implementation(instruction , rd, immediate_value):
    global pc
    rd = register_index[rd]
    imm_val=binaryToDec(immediate_value)
    imm=binaryToDec(imm)
    
    if instruction == "auipc":
        register_values[rd] = imm + pc
    elif instruction == "lui":
        register_values[rd] = imm


# global_var=pc
def i_type_implementation(instruction, rd, rs1, imm):
    rd = register_index[rd]
    rs1 = register_index[rs1]
    imm = binaryToDec(imm)

    if instruction=="lw":
        memory_address = "0x"+hex(register_values[rs1] + imm)[2::].zfill(8)
        register_values[rd] = mem[memory_address]
    elif instruction=="addi":
        register_values[rd] = imm + register_values[rs1]
    elif instruction=="sltiu":
        if(unsigned(register_values[rs1]) < unsigned(imm)):
            register_values[rd]=1
    elif instruction=="jalr":
       register_values[rd] = pc + 4
       pc=register_values[rs1] + imm
def j_type_implementation(instruction, imm, rd):
    global pc
    r_d = register_index[rd]
    imm_val = binaryToDec(imm)

    if instruction=="jal":
        register_values[r_d] = pc + 4
        pc=pc+imm_val
def b_type_implementation(instruction , imm, rs1, rs2):
    global pc
    rs1=register_index[rs1]
    rs2=register_index[rs2]
    imm_val=binaryToDec(imm)
    if instruction=="beq":
        if register_values[rs1]==register_values[rs2]:
            pc=pc+imm_val
        else:
            pc=pc+4

    if instruction=="bne":
        if register_values[rs1]!=register_values[rs2]:
            pc=pc+imm_val
        else:
            pc=pc+4
    if instruction=="blt":
        if register_values[rs1]<register_values[rs2]:
            pc=pc+imm_val
        else:
            pc=pc+4
    if instruction=="bge":
        if register_values[rs1]>register_values[rs2]:
            pc=pc+imm_val
        else:
            pc=pc+4
    if instruction=="bltu":
        if unsigned(register_values[rs1])<unsigned(register_values[rs2]):
            pc=pc+imm_val
        else:
            pc=pc+4
    if instruction=="bgeu":
        if unsigned(register_values[rs1])>unsigned(register_values[rs2]):
            pc=pc+imm_val
        else:
            pc=pc+4




with open(sys.argv[1], "r") as f:
    lines_with_newline = f.readlines()


lines = [line.strip() for line in lines_with_newline]

op_lines = []
pc = 0
while(True):
    if(pc<0 or pc > (len(lines) - 1)/4):
        break
    line = lines[pc/4]
    if line[-7::1] == "0110011":
        r_type_splitting(line)
    elif line[-7::1] in ["0000011", "0010011", "0011011", "0100011"]:
        i_type_splitting(line)
    elif line[-7::1] == "0100011":
        s_type_splitting(line)
    elif line[-7::1] == "1100011":
        #please use global pc here
        b_type_splitting(line)
    elif line[-7::1] in ["0110111", "0010111"]:
        u_type_splitting(line)
    elif line[-7::1] == "1101111":
        j_type_splitting(line)

    pc+=4
    op = "0b"+twosComp32(pc)
    for i in register_values:
        op = op + " 0b" + twosComp32(i)
    op_lines.append(op)

for i in mem:
    op = i + ':' + '0b' + twosComp32(mem[i])
    op_lines.append(op)
    
with open(sys.argv[2], "w") as f:
    f.writelines(op_lines)





