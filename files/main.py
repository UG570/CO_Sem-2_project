def ValidLabel(label):
    #label is not instruction
    # label not in() #fill with dictionary names
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
    for i in range(len(lines)):
        print(lines[i])
        print(labelAdd)
        f.write(InstructionToBinary(lines[i], i))
