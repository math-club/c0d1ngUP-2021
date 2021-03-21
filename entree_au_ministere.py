
from math import sqrt


correct_tupl = ("1", "2", "4", "6", "7")

def main(number):
    
    nb = 64224
    
    number += nb
    number = number**2 
    number = list(str(number))
    
    for n in number:
        if n in correct_tupl:
            pass
        else:
            return 0

    return number

for i in range(1, 1000):
    outp = main(i)
    
    if outp != 0:
        print(sqrt(int("".join(main(i)))))
