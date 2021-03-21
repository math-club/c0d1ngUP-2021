

def code():
    correct_nb = ("1", "2", "4", "6", "7")
    nb = 64224
    answer = []
    while 1:
        nb += 1
        square = nb**2
        correct = list(True for i in range(len(str(square))))
        verif = []
        for i in str(square):
            verif.append(i in correct_nb)
        if verif == correct:
            answer.append(nb)
        if len(answer) == 3:
            return answer


print(code())