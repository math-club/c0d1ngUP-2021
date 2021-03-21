
candy = ["aubergine", "bouillabaisse", "epinards", "chaussette", "glace",
         "foie", "morve de troll", "oeuf pourri", "herbe", "poubelle",
         "saucisse", "vomi"]
         

def main(candy):

    pos = 4

    for i in range(10000):
        c = candy[pos]
        candy[pos] = candy[pos - 1]

        candy[pos - 1] = c
        print(sorted(candy[:4]))
        
        if sorted(candy[:4]) == sorted(["aubergine", "epinards", "glace", "herbe"]):
            return i

        if pos + 5 < 12:
            pos += 5
            
        else :
            pos -= 7


print(main(candy))

# ~ c = candy[1]
# ~ candy[1] = candy[2]

# ~ candy[2] = c

# ~ print(candy)
