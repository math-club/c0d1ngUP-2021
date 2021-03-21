

def retourneur(iterations):
    time = 0
    for i in range(1,iterations):
        sum = 0
        for nb in str(time):
            sum += int(nb)
        if sum != 0 and sum%7 == 0:
            time -= 7
        else:
            time += 2
    return time


print(max([retourneur(i) for i in range(1, 3000)]))
