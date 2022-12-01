from functools import reduce


def get_result(input: list[str]):
    elves = [0]
    current_elve_index = 0

    for line in input:
        if line == "\n":
            elves.append(0)
            current_elve_index += 1
            continue

        elves[current_elve_index] += int(line)

    elves.sort()

    return max(elves), reduce(lambda a, b: a + b, elves[-3:])
