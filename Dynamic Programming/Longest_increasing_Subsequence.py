def longestIncreasingSubsequence(array):
    indices = [None for x in array]
    sequences = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        newLength = binary_search(1, length, indices, array, num)
        sequences[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)
    return build_sequence(sequences, array, indices[length])


def binary_search(start_idx, end_idx, indices, array, num):
    while (start_idx <= end_idx):
        middle_idx = (start_idx + end_idx) // 2

        if (array[indices[middle_idx]] < num):
            start_idx = middle_idx + 1
        else:
            end_idx = middle_idx - 1
    return start_idx


def build_sequence(sequences, array, max_length_idx):
    sequence = []
    while max_length_idx is not None:
        sequence.append(array[max_length_idx])
        max_length_idx = sequences[max_length_idx]
    return list(reversed(sequence))


array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

print(longestIncreasingSubsequence(array))
