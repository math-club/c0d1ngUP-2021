
from itertools import product

light_dict = {
    1 : ((2, 4, 9), (6, 12, 17)),
    2 : ((10, 12, 15), (7, 13, 14)),
    3 : ((2, 16, 20), (5, 7, 18)),
    4 : ((8, 11, 14), (4, 7, 13)),
    5 : ((6, 7, 16), (5, 10, 19)),
    6 : ((2, 10, 13), (5, 8, 14), (6, 19)),
    7 : ((9, 12, 15), (8, 11, 14)),
    8 : ((3, 10, 20), (4, 9, 12), (2, 16)),
    9 : ((4, 5, 12), (1, 15, 19)),
    10 : ((7, 19, 20), (9, 11, 14), (13, 16))
}

LEDS = [0 for i in range(20)]
BOOLS = (0, 1)


def light(leds_tuple):
    
    temp_leds = LEDS
    
    for led in leds_tuple:
        for i in range(3):
            to_change = light_dict[led][0][i] - 1
            current_bool = BOOLS[temp_leds[to_change]]
            temp_leds[to_change] = BOOLS[current_bool - 1]
            
        for j in range(3):
            to_change = light_dict[led][1][j] - 1
            current_bool = BOOLS[temp_leds[to_change]]
            temp_leds[to_change] = 1
            
        try:
            for k in range(3):
                to_change = light_dict[led][2][j] - 1
                current_bool = BOOLS[temp_leds[to_change]]
                temp_leds[to_change] = 0
            
        except IndexError:
            pass
    if temp_leds == [1 for i in range(20)]:

        return True
    else : 
        return False


def generate_tuples():
    #pls
    tuple_list = []
    for i in range(1,6):
        tuple_list += list(product(range(1, 10), repeat = i))
        
    return tuple_list

ok = generate_tuples()

for i in ok:
    
    if light(i) != False:
        print(light(i))
        
print(light((9, 6, 2, 7, 1)))
        
