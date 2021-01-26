def reconstruct_sequence(sequence,array,max_idx):
    current_idx = max_idx
    resulting_sequence = []
    while current_idx != sequence[current_idx]:
        resulting_sequence.append(array[current_idx])
        current_idx = sequence[current_idx]
    resulting_sequence.append(array[current_idx])
    return list(reversed(resulting_sequence))


def maxSumIncreasingSubsequence(array):

    sums = []
    sequence = []
    sums.append(array[0])
    sequence.append(0)
    max_sum = array[0]
    max_idx = 0
    for i in range(1,len(array)):

        previous_idx = i
        max = array[i]
        for j in range(i):
            if array[j] < array[i] and sums[j] + array[i] > max:
                max = sums[j] + array[i]
                previous_idx = j
        sums.append(max)
        sequence.append(previous_idx)
        if max > max_sum:
            max_sum = max
            max_idx = i

    return [max_sum,reconstruct_sequence(sequence,array,max_idx)]







a = [8, 12, 2, 3, 15, 5, 7]

print(maxSumIncreasingSubsequence(a))