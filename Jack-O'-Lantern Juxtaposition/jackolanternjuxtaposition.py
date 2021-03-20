
#Problem ID: jackolanternjuxtaposition
#Author: David Bergendorff
#splits the input into a list of strings consisting of numbers.
#each number is the number of designs for that particular component
#multiplies the number of designs to the achieve the total number of combinations
input = input()
list = input.split()
m = int(list[0])
t = int(list[1])
n = int(list[2])
output = m * t * n
print(output)
