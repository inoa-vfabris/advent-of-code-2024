with open("input.txt") as f:
    a = []  # first numbers of each line
    b = []  # second numbers of each line

    for line in f:
        x, y = map(int, line.split())
        a.append(x)
        b.append(y)

    print("Part 1")
    a.sort()
    b.sort()
    difference = 0
    # add the difference between each number of the first list with the corresponding number of the second list
    for i in range(len(a)):
        difference += abs(a[i] - b[i])
    print(f"The difference between the 2 lists are: {difference}")

    print("Part 2")
    similarity_score = 0
    for i in range(len(a)):
        # gets the number of times a[i] appears in the second list
        count_a = b.count(a[i])
        similarity_score += a[i] * count_a
    print(f"The similarity score is: {similarity_score}")
