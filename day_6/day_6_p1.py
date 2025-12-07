"""
My solution for Day 6 Part 1 of Advent of Code 2025
"""
import math

# file_name = r'advent_of_code_2025\day_6\example_input.txt'
file_name = r'advent_of_code_2025\day_6\input.txt'
with open(file_name, 'r', encoding="utf-8") as file:
    # https://stackoverflow.com/a/49697529/402645
    line_array = file.read().splitlines()
    cell_array = [line.split() for line in line_array]

grand_total = 0

# https://stackoverflow.com/a/59774774/402645
columns = list(zip(*cell_array))

for column in columns:
    op = column[-1]
    column = list(column)
    column.pop()
    column = [int(x) for x in column]

    if op == '+':
        grand_total += int(math.fsum(column))
    elif op == '*':
        grand_total += int(math.prod(column))

print("Grand total:", grand_total)
