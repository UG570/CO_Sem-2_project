from dict import *
from Assembler import u_type,j_type,s_type,r_type,i_type,b_type
def ValidLabel(label_name):
    label = label_name[:-1:]
    if (label not in(r_instruct) and label not in (i_instruct) and label not in (u_instruct) and label not in (j_instruct) and label not in (b_instruct) and label not in (s_instruct)):
        return True
    elif(label_name[-1] == ":"):
        print("instruction name cannot be used as label")
        exit()
    return False

def VirtualHaultCheck(last):
    if last == (["beq", "zero", "zero", "0"]) :
        return True

labelAdd = {}
with open("CO_Sem-2_project\CO Project evaluation framework\CO Project evaluation framework\\automatedTesting\\tests\\assembly\simpleBin\\test1.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        temp = lines[i].strip().split()
        if ((":" in temp[0]) and ValidLabel(temp[0])):
            labelAdd[temp[0][:-1:]] = i
            temp.pop(0)
        
        temp = [temp[0]] + temp[1].split(",")
        lines[i] = temp

if(not(VirtualHaultCheck(lines[-1]))):
    print("Virtual Hault missing")
    exit()

with open("output.txt", "w") as f:
    counter = 0
    for j in range(len(lines)):
        i = lines[j]
        if(j <len(lines) -1 and VirtualHaultCheck(i)):
            print("Virtual Hault at incorrect line")
            exit()
        if i[0] in r_instruct:
            f.write(r_type(regi_dict,function3_r,function_7_r,i,r_instruct))
        elif i[0] in i_instruct:
            f.write(i_type(i, regi_dict,function3_i,i_instruct))
        elif i[0] in u_instruct:
            f.write(u_type(i,regi_dict,u_instruct))
        elif i[0] in j_instruct:
            f.write(j_type(i, counter, labelAdd))
        elif i[0] in b_instruct:
            f.write(b_type(i, counter, labelAdd))
        elif i[0] in s_instruct:
            f.write(s_type(i,regi_dict))
        if j < (len(lines) -1):
            f.write("\n")
        counter += 1

