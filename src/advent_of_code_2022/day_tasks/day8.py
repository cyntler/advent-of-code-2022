def get_result(tree_map: list[str]):
    visible_trees_sum = 0
    highest_scenic_score = 0

    for y, line in enumerate(tree_map):
        for x, char in enumerate(line):
            if x == 0 or x == len(line) - 1 or y == 0 or y == len(tree_map) - 1:
                visible_trees_sum += 1
                continue

            tree = int(char)
            scenic_score_elements = {
                "up": 0,
                "down": 0,
                "left": 0,
                "right": 0,
            }

            trees_around_up = []
            trees_around_down = []
            for y2, line in enumerate(tree_map):
                if y2 <= y - 1:
                    trees_around_up.append(int(line[x]))
                elif y2 >= y + 1:
                    trees_around_down.append(int(line[x]))

            trees_around_left = []
            trees_around_right = []
            for y2, line in enumerate(tree_map):
                if y2 == y:
                    for x2, char2 in enumerate(line):
                        if x2 <= x - 1:
                            trees_around_left.append(int(char2))
                        elif x2 >= x + 1:
                            trees_around_right.append(int(char2))

            trees_around_up.reverse()
            trees_around_left.reverse()

            for trees_around in [
                trees_around_up,
                trees_around_down,
                trees_around_left,
                trees_around_right,
            ]:
                if all(x < tree for x in trees_around):
                    visible_trees_sum += 1
                    break

            for dir, trees_around in [
                ("up", trees_around_up),
                ("down", trees_around_down),
                ("left", trees_around_left),
                ("right", trees_around_right),
            ]:
                for tree_around in trees_around:
                    scenic_score_elements[dir] += 1
                    if tree_around >= tree:
                        break

            scenic_score_multipy_result = 1
            for i in scenic_score_elements:
                scenic_score_multipy_result = (
                    scenic_score_multipy_result * scenic_score_elements[i]
                )

            if scenic_score_multipy_result > highest_scenic_score:
                highest_scenic_score = scenic_score_multipy_result

    return visible_trees_sum, highest_scenic_score
