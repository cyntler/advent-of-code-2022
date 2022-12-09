def get_result(tree_map: list[str]):
    visible_trees_sum = 0

    for y, line in enumerate(tree_map):
        for x, char in enumerate(line):
            if x == 0 or x == len(line) - 1 or y == 0 or y == len(tree_map) - 1:
                visible_trees_sum += 1
                continue

            tree = int(char)

            trees_around_top = []
            trees_around_bottom = []
            for y2, line in enumerate(tree_map):
                if y2 <= y - 1:
                    trees_around_top.append(int(line[x]))
                elif y2 >= y + 1:
                    trees_around_bottom.append(int(line[x]))

            trees_around_left = []
            trees_around_right = []
            for y2, line in enumerate(tree_map):
                if y2 == y:
                    for x2, char2 in enumerate(line):
                        if x2 <= x - 1:
                            trees_around_left.append(int(char2))
                        elif x2 >= x + 1:
                            trees_around_right.append(int(char2))

            for trees_around in [
                trees_around_top,
                trees_around_bottom,
                trees_around_left,
                trees_around_right,
            ]:
                if all(x < tree for x in trees_around):
                    visible_trees_sum += 1
                    break

    return visible_trees_sum
