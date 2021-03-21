

def code():
    correct_set = set("12467")
    nb = 64224
    answer = []
    while 1:
        nb += 1
        square = nb**2
        if set(str(square)) == correct_set:
            answer.append(nb)
        if len(answer) == 3:
            return answer


print(code())