from functools import cache

triangle = open("triangle.txt")

triangle_list = []

for line in triangle:
    nums = [int(num) for num in line.split()]
    triangle_list.append(nums)

print(triangle_list)

@cache
def calc_sum(row, col, curr_sum):
    # base case
    if row == len(triangle_list):
        return curr_sum

    curr_sum += triangle_list[row][col]
    left = calc_sum(row + 1, col, curr_sum)
    right = calc_sum(row + 1, col + 1, curr_sum)

    return max(left, right)

max_sum = calc_sum(0, 0, 0)
print(max_sum)
