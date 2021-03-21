#Problem ID: anotherbrick
#Author: David Bergendorff
#reads the input and creates a list of bricks with the provided length.
#then attempts to build the wall by placing each brick next to each other.
#When a layer is completed, bricks will be placed on the next.
#if a layer ever fails to complete, the program will output "NO" and then stop

first_line = input().split()
second_line = input().split()
height = int(first_line[0])
width = int(first_line[1])
n = int(first_line[2])

bricks = []
for x in range(n):
    bricks.append(int(second_line[x]))
brick_sum_all = sum(bricks)
target = width * height

#if the sum of all bricks is less than the target the wall can't be built
if(brick_sum_all < target):
    print("NO")
else:
    brick_sum = 0
    current_height = 1
    for brick in bricks:
        brick_sum += brick
        if brick_sum > width * current_height:
            print("NO")
            break
        if brick_sum == width*current_height and width*current_height < target:
            current_height += 1
        if current_height == height and brick_sum == target:
            print("YES")
            break
