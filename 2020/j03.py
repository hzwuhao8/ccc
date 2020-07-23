n = int(input())
left_x = -1
left_y = -1
right_x = -1
right_y = -1

for x in range(n):
    (x_str, y_str) = input().split(",")
    x = int(x_str)
    y = int(y_str)
    if x < left_x or left_x == -1:
        left_x = x
    if y < left_y or left_y == -1:
        left_y = y
    if x > right_x:
        right_x = x
    if y > right_y:
        right_y = y

print(left_x - 1, left_y - 1, sep=",")
print(right_x + 1, right_y + 1, sep=",")