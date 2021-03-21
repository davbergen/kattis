
#Problem ID: cups
#Author: David Bergendorff
# reads the input and creates tuples for each cup with the properties radius and color.
# adds the tuples to a list and then sorts the list in increasing order

num_lines = int(input())
list = []
for x in range(num_lines):
    current_line = input()
    pair = current_line.split()
    if(pair[0].isnumeric()):
        radius = int(pair[0])/2
        color = pair[1]
    else:
        radius = int(pair[1])
        color = pair[0]
    tuple = (color, radius)
    list.append(tuple)

list.sort(key=lambda tup: tup[1])
for element in list:
    print(element[0])
