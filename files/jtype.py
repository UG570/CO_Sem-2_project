def jtype(instruction):
    register = instruction[1::]
    t=sextUJ(int(register[1]))
    return t[0]+t[9:20]+t[9]+t[1:8]+regi_dict[register[0]]+"0010111"