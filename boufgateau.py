
gr_list = [6, 13, 21, 2, 19, 23, 24, 22, 10, 25, 16, 11, 18, 14, 1, 5, 20, 3, 26, 28]

def main():
    
    for i in range(20):

        for k in range(4):
            for j in range(5):
                temp = gr_list
                
                temp[(k*4 + j)] = cur
                temp[(k*4 + j)] = temp[i]
                temp[i] = cur
