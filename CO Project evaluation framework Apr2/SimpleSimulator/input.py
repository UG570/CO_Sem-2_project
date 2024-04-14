
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






