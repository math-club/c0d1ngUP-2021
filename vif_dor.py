

def vif(n):
    start = (0, 0, 1)
    position = (start[1], start[2], sum(start) % n)
    i = 1
    while position != (0, 0, 1):
        position = (position[1], position[2], sum(position) % n)
        i += 1
        print(position)
    return i


length = []
for i in range(2,201):
    length.append((vif(i), i))
    print(i)

values_list = []
for i in length:
    values_list.append(i[0])
print(values_list)
print(max(values_list))
print(values_list.index(max(values_list)))

gold_values = []
for i in range(10):
    print(max(values_list))
    print(values_list.index(max(values_list)))
    gold_values.append(values_list.index(max(values_list)) + 2)
    values_list[values_list.index(max(values_list))] = 0
print(gold_values)