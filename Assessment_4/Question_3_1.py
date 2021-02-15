def countContainedPermutations(bigString, smallString):
    original_char_map = {}

    for char in smallString:
        if char in original_char_map:
            original_char_map[char] += 1
        else:
            original_char_map[char] = 1


    possible_matches = []
    count = 0
    for i in range(len(bigString)):
        current_char = bigString[i]
        if current_char in original_char_map:
            possible_matches.append(original_char_map.copy())
            elements_to_keep = []
            for j in range(len(possible_matches)):

                possible_match = possible_matches[j]
                if current_char in possible_match:
                    possible_match[current_char] -= 1
                    if possible_match[current_char] == 0:
                        possible_match.__delitem__(current_char)
                    if possible_match:
                        count +=1
                        continue
                    elements_to_keep.append(j)
            possible_matches = [possible_matches[p] for p in elements_to_keep]



    return count
