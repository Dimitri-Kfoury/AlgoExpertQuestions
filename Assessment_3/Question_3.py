def buildFailures(buildRuns):
    percentages = []

    for buildrun in buildRuns:
        percentages.append(get_percentage(buildrun))
    print(percentages)
    streaks = []
    streaks.append(1)
    for i in range(1, len(percentages)):
        if percentages[i] < percentages[i - 1]:
            streaks.append(streaks[i - 1] + 1)
        else:
            streaks.append(1)
    result = max(streaks)

    return result if result > 1 else -1


def get_percentage(buildrun):
    total_hours = len(buildrun)

    mid_index = (total_hours - 1) // 2
    upper = total_hours - 1
    lower = 0
    while upper >= lower:
        if buildrun[mid_index]:
            lower = mid_index + 1
            mid_index = (upper + lower) // 2
        else:
            upper = mid_index - 1
            mid_index = (upper + lower) // 2
    return ((upper + 1) / total_hours) * 100


buildruns = [
    [True, True, True, False, False],
    [True, True, True, True, False],
    [True, True, True, True, True, True, False, False, False],
    [True, False, False, False, False, False],
    [True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     True,
     False
     ],
    [True, False],
    [True, True, True, True, False, False],
    [True, True, True, True, True, True, True, True, True, False],
    [True, True, True, True, True, True, True, True, False, False],
    [True, True, True, True, True, True, True, False, False, False],
    [True, True, True, True, True, True, False, False, False, False],
    [True, True, True, True, True, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, False]
]

print(buildFailures(buildruns))
