def is_command(line: str):
    return "$" in line


def get_command_segments(line: str):
    segments = line.split(" ")

    if len(segments) > 2:
        return segments[1], segments[2]
    else:
        return segments[1], None


def get_index_list(terminal_output: list[str], index: int) -> list[str]:
    list = []

    for line in terminal_output[(index + 1) :]:
        if is_command(line):
            break
        list.append(line)

    return list


def parse_terminal_output(terminal_output: list[str]):
    three = []
    current_dir = ""

    for index, line in enumerate(terminal_output):
        if is_command(line):
            command, param = get_command_segments(line)
            match command:
                case "cd":
                    if param == "..":
                        if current_dir != "/":
                            new_dir_list = current_dir.split("/")[:-1]
                            current_dir = (
                                "/"
                                if len(new_dir_list) == 1
                                else "/".join(new_dir_list)
                            )
                    else:
                        if current_dir == "":
                            current_dir = param
                        else:
                            if current_dir == "/":
                                current_dir = current_dir + param
                            else:
                                current_dir = current_dir + "/" + param
                case "ls":
                    index_list = get_index_list(terminal_output, index)
                    for item in index_list:
                        [type, name] = item.split(" ")

                        three_target = three
                        current_dir_segments = current_dir.split("/")
                        if len(current_dir_segments) > 0:
                            for segment in current_dir_segments:
                                three_dir = list(
                                    filter(
                                        lambda item: item["type"] == "dir"
                                        and item["name"] == segment,
                                        three_target,
                                    )
                                )
                                if len(three_dir) > 0:
                                    three_target = three_dir[0]["children"]

                        if type == "dir":
                            three_target.append(
                                {"type": "dir", "name": name, "children": []}
                            )
                        else:
                            three_target.append(
                                {"type": "file", "name": name, "weight": int(type)}
                            )

    return three


def get_size_of_three_files(three: list):
    size = 0

    for item in three:
        if item["type"] == "file":
            size += item["weight"]

    return size


def get_size_of_dir(dir_three: list):
    dir_size = get_size_of_three_files(dir_three)

    if len(dir_three["children"]) > 0:
        dir_size += get_size_of_dir(dir_three["children"])

    return dir_size


def calculate_dir_total_size_at_most_100000(three: list):
    size_of_root = get_size_of_three_files(three)
    total_size = size_of_root if size_of_root <= 100000 else 0

    for item in three:
        dir_size = get_size_of_dir(item)
        if dir_size <= 100000:
            total_size += total_size

    return total_size


def get_result(terminal_output: list[str]):
    three = parse_terminal_output(terminal_output)
    return calculate_dir_total_size_at_most_100000(three)
