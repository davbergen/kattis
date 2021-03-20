import sys
#Problem ID:  greetings2
#author: David Bergendorff
#reads he...ey from input and multiplies the number of e's by two
for line in sys.stdin:
    input = line
    output = input[0]
    for element in input:
        if(element == 'e'):
            output += 'ee'
    output += 'y'
    print(output)
