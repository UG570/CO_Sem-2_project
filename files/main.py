from dict import *
from Assembler import u_type,j_type,s_type,r_type,i_type,b_type
def ValidLabel(label):
    if (label not in(r_instruct) and label not in (i_instruct) and label not in (u_instruct) and label not in (j_instruct) and label not in (b_instruct) and label not in (s_instruct)):
        return True
def InstructionToBinary(l,n):
    return " done \n" #import from assembler
labelAdd = {}
with open("CO_Sem-2_project\CO Project evaluation framework\CO Project evaluation framework\\automatedTesting\\tests\\assembly\simpleBin\\test3.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        temp = lines[i].strip().split()
        if ((":" in temp[0]) and ValidLabel(temp[0][-1])):
            labelAdd[temp[0][:-1:]] = i
            temp.pop(0)
        
        temp = [temp[0]] + temp[1].split(",")
        lines[i] = temp

with open("output.txt", "w") as f:
    counter = 0
    for i in lines:
        if i[0] in r_instruct:
            f.write(r_type(regi_dict,function3_r,function_7_r,i,r_instruct))
            f.write("\n")
        elif i[0] in i_instruct:
            f.write(i_type(i, regi_dict,function3_i,i_instruct))
            f.write("\n")
        elif i[0] in u_instruct:
            f.write(u_type(i,regi_dict,u_instruct))
            f.write("\n")
        elif i[0] in j_instruct:
            f.write(j_type(i))
            f.write("\n")
        elif i[0] in b_instruct:
            f.write(b_type(i, counter, labelAdd))
            f.write("\n")
        elif i[0] in s_instruct:
            f.write(s_type(i,regi_dict))
            f.write("\n")
        counter += 1

