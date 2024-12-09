import re

with open("input.txt") as f:
    total_sum = 0
    total_sum_enabled = 0

    pattern = re.compile(r"mul\((-?\d+),(-?\d+)\)|(do\(\))|(don't\(\))")
    matches = pattern.findall(f.read())

    do = True
    for a, b, do_match, dont_match in matches:
        if do_match:
            do = True
        elif dont_match:
            do = False
        else:
            res = int(a) * int(b)
            total_sum += res
            total_sum_enabled += res * do

    print("Part 1")
    print(f"The sum of all multiplication is: {total_sum}")
    print("Part 2")
    print(f"The sum of only the enabled multiplication is: {total_sum_enabled}")
