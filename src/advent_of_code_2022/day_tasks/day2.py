opponent_shapes = {
    "rock": "A",
    "paper": "B",
    "scissors": "C",
}

my_shapes = {
    "rock": "X",
    "paper": "Y",
    "scissors": "Z",
}


def is_rock(shape: str):
    return shape == opponent_shapes["rock"] or shape == my_shapes["rock"]


def is_paper(shape: str):
    return shape == opponent_shapes["paper"] or shape == my_shapes["paper"]


def is_scissors(shape: str):
    return shape == opponent_shapes["scissors"] or shape == my_shapes["scissors"]


def get_round_shapes(round: str):
    return round.split(" ")


def get_lose_shape(shape: str):
    if shape == opponent_shapes["paper"]:
        return my_shapes["rock"]
    if shape == opponent_shapes["scissors"]:
        return my_shapes["paper"]
    if shape == opponent_shapes["rock"]:
        return my_shapes["scissors"]


def get_draw_shape(shape: str):
    opponent_key = [k for k, v in opponent_shapes.items() if v == shape][0]
    return my_shapes[opponent_key]


def get_win_shape(shape: str):
    if shape == opponent_shapes["rock"]:
        return my_shapes["paper"]
    if shape == opponent_shapes["paper"]:
        return my_shapes["scissors"]
    if shape == opponent_shapes["scissors"]:
        return my_shapes["rock"]


def part_two_rounds_mapper(round: str):
    [opponent_shape, my_shape] = get_round_shapes(round)
    new_shape = ""

    if my_shape == my_shapes["rock"]:
        new_shape = get_lose_shape(opponent_shape)
    elif my_shape == my_shapes["paper"]:
        new_shape = get_draw_shape(opponent_shape)
    else:
        new_shape = get_win_shape(opponent_shape)

    return opponent_shape + " " + new_shape


def get_my_total_score(rounds: list[str]):
    total_score = 0

    for round in rounds:
        [opponent_shape, my_shape] = get_round_shapes(round)

        if is_rock(my_shape):
            total_score += 1
        elif is_paper(my_shape):
            total_score += 2
        elif is_scissors(my_shape):
            total_score += 3

        if (
            (is_rock(my_shape) and is_rock(opponent_shape))
            or (is_paper(my_shape) and is_paper(opponent_shape))
            or (is_scissors(my_shape) and is_scissors(opponent_shape))
        ):
            total_score += 3
        else:
            if (
                (is_rock(my_shape) and is_scissors(opponent_shape))
                or (is_scissors(my_shape) and is_paper(opponent_shape))
                or (is_paper(my_shape) and is_rock(opponent_shape))
            ):
                total_score += 6

    return total_score


def get_result(rounds: list[str]):
    part_two_rounds = map(part_two_rounds_mapper, rounds)
    return get_my_total_score(rounds), get_my_total_score(part_two_rounds)
