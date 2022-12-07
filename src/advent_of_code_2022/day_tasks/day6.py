from iteration_utilities import unique_everseen, duplicates


def detect_start_of_packet_marker(signal: str, distinct_chars_count=4):
    current_letters = []
    first_marker = 0
    for index, char in enumerate(signal):
        current_letters.append(char)
        if len(current_letters) == distinct_chars_count:
            if len(list(unique_everseen(duplicates(current_letters)))) > 0:
                current_letters.pop(0)
                continue
            else:
                first_marker = index + 1
                break

    print(current_letters)
    return first_marker


def get_result(signal: str):
    return detect_start_of_packet_marker(signal), detect_start_of_packet_marker(
        signal, 14
    )
