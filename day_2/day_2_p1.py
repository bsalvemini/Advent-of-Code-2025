"""
My solution for Day 2 Part 1 of Advent of Code 2025
"""
import csv

invalid_id_sum = 0

# file_name = 'example_input.txt'
file_name = 'input.txt'

with open(file_name, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    ranges = list(reader)[0]

for r in ranges:

    range_parts = r.split('-')
    start = int(range_parts[0])
    end = int(range_parts[1])

    for i in range(start, end + 1):
        length = len(str(i))
        half_length = length // 2
        if length % 2 != 0:
            continue
        num_p1 = str(i)[:half_length]
        num_p2 = str(i)[half_length:]
        if num_p1 == num_p2:
            print(f"Invalid id: {i}")
            invalid_id_sum += i

print("Total:", invalid_id_sum)
