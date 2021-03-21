

correct_tupl = ("1", "2", "4", "6", "7")

def main(number):
    
    nb = 64224
    
    at = number
    number = number**2 
    number = list(str(number))
    
    for n in number:
        if n in correct_tupl:
            pass
        else:
            return 0

    return at

nb_list = [number + 64224 for number in range(1, 1000)]

for i in nb_list:
    outp = main(i)
    
    if outp:
        print(main(i))
