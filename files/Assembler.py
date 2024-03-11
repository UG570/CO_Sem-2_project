#Assembler made in python
# write functions for all types here
def r_type(regi_dict,function3_r,function7_r,instruction,r_instruct):
    return function7_r[instruction[0]]+regi_dict[instruction[3]]+regi_dict[instruction[2]]+function3_r[instruction[0]]+regi_dict[instruction[1]]+r_instruct[instruction[0]]
def utype(instruction,regi_dict,u_instruct):
    opcode=u_instruct[instruction[0]]
    t=sextU(int(instruction[2]))
    return t+regi_dict[instruction[1]+opcode
