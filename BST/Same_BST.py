def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo) or arrayOne[0] != arrayTwo[0]:
        return False
    return bts(0, 0, float("-inf"), float("+inf"), arrayOne, arrayTwo)


def bts(index1, index2, min, max, arrayOne, arrayTwo):
    currentElement = arrayOne[index1]
    firstGreater = None
    secondGreater = None

    for i in range(index1 + 1, len(arrayOne)):
        if currentElement <= arrayOne[i] < max:
            firstGreater = i
            break
    for i in range(index2 + 1, len(arrayOne)):
        if currentElement <= arrayTwo[i] < max:
            secondGreater = i
            break

    firstSmaller = None
    secondSmaller = None

    for i in range(index1 + 1, len(arrayOne)):
        if currentElement > arrayOne[i] >= min:
            firstSmaller = i
            break
    for i in range(index2 + 1, len(arrayOne)):
        if currentElement > arrayTwo[i] >= min:
            secondSmaller = i
            break

    if (firstGreater is not None and secondGreater is not None and not arrayOne[firstGreater] == arrayTwo[
        secondGreater]) \
            or (firstGreater is None and secondGreater is not None) or (
            secondGreater is None and firstGreater is not None):
        return False;

    if firstSmaller is not None and secondSmaller is not None and not arrayOne[firstSmaller] == arrayTwo[
        secondSmaller] or \
            (firstSmaller is None and secondSmaller is not None) or (
            secondSmaller is None and firstSmaller is not None):
        return False;

    if firstGreater is not None and firstSmaller is not None:
        return bts(firstGreater, secondGreater, currentElement, max, arrayOne, arrayTwo) and bts(firstSmaller,
                                                                                                 secondSmaller, min,
                                                                                                 currentElement,
                                                                                                 arrayOne, arrayTwo)
    elif firstGreater is None and firstSmaller is None:
        return True
    elif firstGreater is not None and firstSmaller is None:
        return bts(firstGreater, secondGreater, currentElement, max, arrayOne, arrayTwo)
    else:
        return bts(firstSmaller, secondSmaller, min, currentElement, arrayOne, arrayTwo)

