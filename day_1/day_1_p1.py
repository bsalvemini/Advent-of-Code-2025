"""
My solution for Day 1 Part 1 of Advent of Code 2025
"""

class Rotation:
    def __init__(self, direction, rotate_num):
        self.direction = direction
        self.rotate_num = rotate_num

    def __str__(self):
        return f"Direction: {self.direction} Rotate to: {self.rotate_num}"

def split_rotation(rot):
    rot_obj = Rotation("L", 0)
    for _ in rot:
        rot_obj.direction = rot[0]
        rot_obj.rotate_num = int(rot[1:])
    return rot_obj

# file_name = 'example_input.txt'
file_name = 'input.txt'
rotations = []
with open(file_name, 'r', encoding="utf-8") as file:
    rotations = file.read().splitlines()

dial_nums = list(range(0, 100))
rot_objs = [split_rotation(x) for x in rotations]
zero_count = 0
start_pos = dial_nums[50]
current_pos = start_pos

for o in rot_objs:
    if o.direction == 'L':
        print(f"Rotate left to {o.rotate_num}")
        if current_pos + o.rotate_num > (len(dial_nums) - 1):
            index = (current_pos - o.rotate_num) % len(dial_nums)
            print("index: ", index)
        else:
            index = current_pos - o.rotate_num
            print("index: ", index)
        current_pos = dial_nums[index]
    elif o.direction == 'R':
        print(f"Rotate right to {o.rotate_num}")
        if current_pos + o.rotate_num > (len(dial_nums) - 1):
            index = (current_pos + o.rotate_num) % len(dial_nums)
            print("index: ", index)
        else:
            index = current_pos + o.rotate_num
            print("index: ", index)
        current_pos = dial_nums[index]
    else:
        pass
    if current_pos == 0:
        zero_count += 1
    print(f"Current position: {current_pos}")

print("Password:", zero_count)
