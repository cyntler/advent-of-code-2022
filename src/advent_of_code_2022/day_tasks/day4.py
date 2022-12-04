def get_result(section_assignment_pairs: list[str]):
    fully_contains_sum = 0

    for pair in section_assignment_pairs:
        pair_split = pair.split(",")
        [num11, num12] = map(lambda num: int(num), pair_split[0].split("-"))
        [num21, num22] = map(lambda num: int(num), pair_split[1].split("-"))

        if (num11 <= num21 and num12 >= num22) or (num21 <= num11 and num22 >= num12):
            fully_contains_sum += 1

    return fully_contains_sum
