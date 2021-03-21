
#SVP NE REGARDEZ PAS C'EST HORRIBLE VRAIMENT RECULEZ J'AI HONTE PARDON

def main(ar_gallion):
    
    ar_gallion = ar_gallion
    ar_mornille = ar_gallion*17
    ar_noises = ar_mornille*29
    
    ar_gallion, ar_mornille, ar_noises = str(ar_gallion),str(ar_mornille), str(ar_noises)
    
    #ahaahha
    for i in ar_gallion:
        if i in ar_mornille:
            if i in ar_noises:
                pass
            else :
                return 0
        else :
            return 0
            
    for j in ar_mornille:
        if j in ar_gallion:
            if j in ar_noises:
                pass
            else :
                return 0
        else :
            return 0
            
    for k in ar_noises:
        if k in ar_mornille:
            if k in ar_gallion:
                pass
            else :
                return 0
        else :
            return 0

    return ar_gallion
    
#AHHHHHHH
for i in range(10000000):
    
    if main(i) != 0:
        print(main(i))
