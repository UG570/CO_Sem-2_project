
register_index = {'00000': 0, '00001': 1, '00010': 2, '00011': 3, '00100': 4, '00101': 5, '00110': 6,
                    '00111': 7, '01000': 8, '01001': 9, '01010': 10, '01011': 11, '01100': 12, '01101': 13,
                    '01110': 14, '01111': 15, '10000': 16, '10001': 17, '10010': 18, '10011': 19, '10100': 20,
                    '10101': 21, '10110': 22, '10111': 23, '11000': 24, '11001': 25, '11010': 26, '11011': 27,
                    '11100': 28, '11101': 29, '11110': 30, '11111': 31}
register_values = [0]*32

def unsigned(num):
    return ((num + 2**32) & 0b11111111111111111111111111111111)
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
    i_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])


def s_type_splitting(str):
    # global instruction
    if str[-15:-12:1]== "010":
            instruction="sw"
    s_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])


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
    b_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])


def u_type_splitting(str):
    if str[0:7]=="0110111":
        instruction="lui"
    else:
        instruction="auipc"
    u_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])


def j_type_splitting(str):
    if str[0:7]=="1101111":
        instruction="jal"
    j_type_implementation(instruction ,str[-12:-7:1], str[-20:-15:1], str[-25:-20:1])

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

with open(
        "CO_Sem-2_project\CO Project evaluation framework\CO Project evaluation framework\\automatedTesting\\tests\\assembly\simpleBin\\test1.txt",
        "r") as f:
    lines_with_newline = f.readlines()


lines = [line.strip() for line in lines_with_newline]


for line in lines:
    if line[-7::1] == "0110011":
        r_type_splitting(line)
    elif line[-7::1] in ["0000011", "0010011", "0011011", "0100011"]:
        i_type_splitting(line)
    elif line[-7::1] == "0100011":
        s_type_splitting(line)
    elif line[-7::1] == "1100011":
        b_type_splitting(line)
    elif line[-7::1] in ["0110111", "0010111"]:
        u_type_splitting(line)
    elif line[-7::1] == "1101111":
        j_type_splitting(line)
    else:
        continue






