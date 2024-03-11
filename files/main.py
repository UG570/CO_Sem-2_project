from dict import *
from Assembler import *
def ValidLabel(label):
    if (label not in(r_instruct) and label not in (i_instruct) and label not in (u_instruct) and label not in (j_instruct) and label not in (b_instruct) and label not in (s_instruct)):
        return True
def InstructionToBinary(l,n):
    return " done \n" #import from assembler
labelAdd = {}
with open("CO Project evaluation framework\CO Project evaluation framework\\automatedTesting\\tests\\assembly\simpleBin\\test3.txt", "r") as f:
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
            f.writeline(r_type(i))
        elif i[0] in i_instruct:
            f.writeline(i_type(i))
        elif i[0] in u_instruct:
            f.writeline(u_type(i))
        elif i[0] in j_instruct:
            f.writeline(j_type(i))
        elif i[0] in b_instruct:
            f.writeline(b_type(i, counter))
        elif i[0] in s_instruct:
            f.writeline(s_type(i))
        counter += 1

