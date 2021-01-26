def longestStringChain(strings):
    strings_map = {}
    max_length_start = None
    max_length = 0
    visited = {}
    strings.sort(key=len)
    for string in strings:
        strings_map[string] = string

    for string in strings:
        local_max = 0
        local_previous = None
        for i in range(0, len(string)):
            substring = string[0:i] + string[i + 1:len(string)]
            if substring in strings_map.keys():
                current_length = visited[substring][0] + 1
                if current_length > local_max:
                    local_max = current_length
                    local_previous = substring
        if local_previous is not None:
            visited[string] = [local_max, local_previous]
            if local_max > max_length:
                max_length = local_max
                max_length_start = string
        else:
            visited[string] = [0, None]
    return build_sequence(max_length_start,visited)


def build_sequence(max_length_start, visited):
    current_string = max_length_start
    sequence = []
    while current_string is not None:
        sequence.append(current_string)
        current_string = visited[current_string][1]
    return sequence


strings = [
    "abcdefg1",
    "1234c",
    "abdefg2",
    "abdfg",
    "123",
    "122",
    "bgg",
    "g",
    "1a2345",
    "12a345"
]

print(longestStringChain(strings))