def get_numbers(pair: str):
    pair_split = pair.split(",")
    [num11, num12] = map(lambda num: int(num), pair_split[0].split("-"))
    [num21, num22] = map(lambda num: int(num), pair_split[1].split("-"))

    return num11, num12, num21, num22


def get_fully_contains_sum(section_assignment_pairs: list[str]):
    fully_contains_sum = 0

    for pair in section_assignment_pairs:
        num11, num12, num21, num22 = get_numbers(pair)

        if (num11 <= num21 and num12 >= num22) or (num21 <= num11 and num22 >= num12):
            fully_contains_sum += 1

    return fully_contains_sum


def get_overlap_sum(section_assignment_pairs: list[str]):
    overlap_sum = 0

    for pair in section_assignment_pairs:
        num11, num12, num21, num22 = get_numbers(pair)

        range1 = list(range(num11, num12 + 1))
        range2 = list(range(num21, num22 + 1))

        for num in range1:
            if num in range2:
                overlap_sum += 1
                break

    return overlap_sum


def get_result(section_assignment_pairs: list[str]):
    return get_fully_contains_sum(section_assignment_pairs), get_overlap_sum(
        section_assignment_pairs
    )
