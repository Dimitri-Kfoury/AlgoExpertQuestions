def knapsackProblem(items, capacity):
    knapsack_values = [[0 for i in range(0, capacity + 1)] for c in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        current_weight = items[i - 1][1]
        current_value = items[i - 1][0]
        for c in range(0, capacity + 1):
            if current_weight > c:
                knapsack_values[i][c] = knapsack_values[i - 1][c]
            else:
                knapsack_values[i][c] = max(knapsack_values[i - 1][c],
                                            knapsack_values[i - 1][c - current_weight] + current_value)

    return [knapsack_values[-1][-1],get_items(knapsack_values,items)]


def get_items(knapsack_values, items):
    i = len(items)
    c = len(knapsack_values[0]) - 1
    sequence = []

    while i > 0:
        if knapsack_values[i][c] == knapsack_values[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))
