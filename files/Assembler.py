#Assembler made in python
# write functions for all types here
def r_type(regi_dict,function3_r,function7_r,instruction,r_instruct):
    return function7_r[instruction[0]]+regi_dict[instruction[3]]+regi_dict[instruction[2]]+function3_r[instruction[0]]+regi_dict[instruction[1]]+r_instruct[instruction[0]]
