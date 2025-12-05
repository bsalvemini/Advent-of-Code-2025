"""
My solution for Day 5 Part 1 of Advent of Code 2025
"""

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return(f"{self.start}-{self.end}")


def create_range(range):
    range_obj = Range(0, 1)
    for _ in range:
        range_parts = range.split('-')
        range_obj.start = int(range_parts[0])
        range_obj.end = int(range_parts[1])
    return range_obj

# file_name = r'advent_of_code_2025\day_5\example_input.txt'
file_name = r'advent_of_code_2025\day_5\input.txt'
with open(file_name, 'r', encoding="utf-8") as file:
    data = file.read().splitlines()
    ranges = data[:data.index('')]
    ingredient_ids = data[data.index('') + 1:]

fresh_ingredients = []
fresh_count = 0
# print(data)

print("ranges:", ranges)
print("ids:", ingredient_ids)

print("ranges:", len(ranges))
print("ids:", len(ingredient_ids))

range_objs = [create_range(x) for x in ranges]

# print("Range:", range_objs[0])
print("Ingredient IDs:", ingredient_ids)

for range in range_objs:
    print("Current range:", range)

    for ingredient_id in ingredient_ids:
        if range.start <= int(ingredient_id) <= range.end:
            if not ingredient_id in fresh_ingredients:
                fresh_ingredients.append(ingredient_id)

fresh_count = len(fresh_ingredients)
print("Fresh Ingredients:", fresh_ingredients)
print("fresh_count:", fresh_count)