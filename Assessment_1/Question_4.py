def longestStreakOfAdjacentOnes(array):
    max_streak = 0
    max_streak_idx = -1

    for i in range(len(array)):
        if array[i] == 0:
            streak = get_streak(i, array)
            if streak > max_streak:
                max_streak = streak
                max_streak_idx = i
    return max_streak_idx



def get_streak(i,array):
    left = i - 1
    right = i + 1
    count  = 1

    while left >= 0 and array[left] == 1:
        left -=1
        count+=1
    while right < len(array) and array[right] == 1:
        right +=1
        count+=1
    return count


array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]

print(longestStreakOfAdjacentOnes(array))