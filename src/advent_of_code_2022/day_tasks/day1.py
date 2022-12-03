from functools import reduce


def get_result(calories: list[str]):
    elves = [0]
    current_elve_index = 0

    for calorie in calories:
        if calorie == "":
            elves.append(0)
            current_elve_index += 1
            continue

        elves[current_elve_index] += int(calorie)

    elves.sort()

    return max(elves), reduce(lambda a, b: a + b, elves[-3:])
