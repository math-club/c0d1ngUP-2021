
language = {
    "HFH" : "A",
    "FFH" : "B",
    "SHS" : "C",
    "SHH" : "D",
    "SSH" : "E",
    "FHF" : "F",
    "FSS" : "G",
    "HFF" : "H",
    "HHH" : "I",
    "SFS" : "K",
    "FFS" : "L",
    "FHS" : "M",
    "SSF" : "N",
    "FHH" : "O",
    "HHF" : "P",
    "SFF" : "Q",
    "FSF" : "R",
    "FSH" : "S",
    "HHS" : "T",
    "FFF" : "U",
    "SSS" : "W",
    "HFS" : "X",
    "SHF" : "Y",
    "SFH" : "Z",
}


def main(message):
    message = list(message)
    outp = []

    while len(message):
        
        if "".join((message[0], message[1])) == "HS": 
            print("".join((message[0], message[1])))
            outp.append(" ")
            del message[1]
            del message[0]
        
        else:
            outp.append(language["".join((message[0], message[1], message[2]))])
            print(language["".join((message[0], message[1], message[2]))])
            del message[2]
            del message[1]
            del message[0]
            
            
    return outp

print("".join(main("FHSFHHSSFHSSHSHFFSSHFSFHSSSFHFHFSSFFFHHHSSFHHHHSSHHSSHFHSHFHHHHSSFHSSSHFSHHHSHSFFFSSFHSFSSFSFHFHSSFSHHHSHHHFHHFFFFSFHSHHFFHHFFFFSFHSSSFFHHFFFFSHHSSHSHFHFSFHSSSFFHHFFFFSHHSHFHFFSFFSFHHSSFFSHHSSSHSSFFHFHHHSSFHSHHFFHHFFFFFFFHHHHHFSFHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFHSSHHSSHHSSHSSSHFSHHSHHSFSFFHHHHHFSHHSHHHFSSSSFFHHFFHFFSSSHFSHHSHHSFSFHFHHHHHHSFSFSSHFSHHSSSHHHSHSFFSFHHFSFFSHSFFFFFSSHHSHHSHFFSSHFHHSHHHFHFSFSHHHSHFHFFSHFHFSHHHSFHHFSFHSSSHHHSHSSHSFHHFSFFHSHFHSHSHSSSFSSHHSSSFFHHFFFFSHHSFSSSSHSSFSSHFSFFHHSSFHHSHSHHFFFSFFFFSHHSSSFFHHFFFFSHHSSSFFHHFFFFSHHSFHHSHSSHSFFFHHFSSHFSFFHHSSFFSHHSSHHSSHFSHHSHFHFFFHHSFSFSSHFSH")))
        
        
