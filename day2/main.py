def is_ordered(level_list: list[int]) -> bool:
    ascending_list = sorted(set(level_list))
    descending_list = sorted(set(level_list), reverse=True)
    return level_list in [ascending_list, descending_list]


def is_correctly_spaced(level_list: list[int]) -> bool:
    # verify if any two adjacent levels differ by at least 1 and at most 3
    level_list_size = len(level_list) - 1
    is_safe = True
    for i in range(len(level_list)):
        if i + 1 <= level_list_size:
            next_level = level_list[i + 1]
            level = level_list[i]
            if abs(level - next_level) > 3:
                is_safe = False
    return is_safe


with open("input.txt") as f:
    number_of_safe_reports = 0
    for line in f:
        level_list = list(map(int, line.split()))
        if is_ordered(level_list) and is_correctly_spaced(level_list):
            number_of_safe_reports += 1
    print("Part 1")
    print(f"Number of safe reports: {number_of_safe_reports}")


def dampener_technique(level_list: list[int]) -> bool:
    # is safe if removing only one level makes the list ordered and correctly spaced
    is_safe = False
    for level in range(len(level_list)):
        tolerated_levels = level_list[:level] + level_list[level + 1 :]
        if is_ordered(tolerated_levels) and is_correctly_spaced(tolerated_levels):
            is_safe = True
    return is_safe

with open("input.txt") as f:
    print("Part 2")
    number_of_safe_reports = 0
    for line in f:
        level_list: list[int] = list(map(int, line.split()))
        if is_ordered(level_list) and is_correctly_spaced(level_list):
            number_of_safe_reports += 1
        elif dampener_technique(level_list):
            number_of_safe_reports += 1
    print(f"Number of safe reports: {number_of_safe_reports}")
