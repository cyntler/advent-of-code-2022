import re
from functools import reduce


def parse_rearrangement_procedure(rearrangement_procedure: list[str]):
    shape = {}
    instructions = []

    for i, line in enumerate(rearrangement_procedure):
        if line.replace(" ", "").isdigit():
            for j, char in enumerate(line):
                if char.isdigit():
                    char_as_int = int(char)
                    shape[char_as_int] = []
                    for x in range(0, i):
                        if (
                            rearrangement_procedure[x] != ""
                            and len(rearrangement_procedure[x]) - 1 >= j
                            and rearrangement_procedure[x][j].strip() != ""
                        ):
                            shape[char_as_int].append(rearrangement_procedure[x][j])
                            None

        if "move" in line:
            instructions.append([int(s) for s in re.findall(r"\d+", line)])

    return (shape, instructions)


def get_crate_top_of_each_stack(rearrangement_procedure: list[str]):
    shape, instructions = parse_rearrangement_procedure(rearrangement_procedure)

    for ins in instructions:
        [count, from_num, to_num] = ins
        for _ in range(0, count):
            shape.get(to_num).insert(0, shape.get(from_num).pop(0))

    return reduce(lambda x, value: x + value[0], shape.values(), "")


def get_result(rearrangement_procedure: list[str]):
    return get_crate_top_of_each_stack(rearrangement_procedure)
