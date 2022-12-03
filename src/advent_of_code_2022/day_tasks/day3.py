import string


def letter_to_number(letter: str):
    if letter.isupper():
        return string.ascii_uppercase.index(letter) + 27

    return string.ascii_lowercase.index(letter) + 1


def get_compartment_pairs(rucksacks: list[str]):
    compartment_pairs = []
    for rucksack in rucksacks:
        compartment1, compartment2 = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )
        compartment_pairs.append([compartment1, compartment2])

    return compartment_pairs


def get_three_elf_split_compartments(rucksacks: list[str]):
    compartment_threes = []
    print(len(rucksacks))
    for i, rucksack in enumerate(rucksacks):
        if (i + 1) % 3 == 0:
            compartment_threes.append(
                [
                    rucksacks[i - 2],
                    rucksacks[i - 1],
                    rucksacks[i],
                ]
            )

    return compartment_threes


def get_rucksack_priorities_sum(rucksacks: list[str]):
    compartment_pairs = get_compartment_pairs(rucksacks)
    priorities_sum = 0

    for [compartment1, compartment2] in compartment_pairs:
        for l in compartment1:
            if l in compartment2:
                num = letter_to_number(l)
                priorities_sum += num
                break

    return priorities_sum


def get_three_elf_priorities_sum(rucksacks: list[str]):
    compartment_threes = get_three_elf_split_compartments(rucksacks)
    priorities_sum = 0

    for [compartment1, compartment2, compartment3] in compartment_threes:
        for l in compartment1:
            if l in compartment2 and l in compartment3:
                num = letter_to_number(l)
                priorities_sum += num
                break

    return priorities_sum


def get_result(rucksacks: list[str]):
    return get_rucksack_priorities_sum(rucksacks), get_three_elf_priorities_sum(
        rucksacks
    )
