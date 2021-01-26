def productSum(array):
    return productS(array,1)


def productS(array, depth):
    sum = 0

    for element in array:
        if type(element) is list:
            sum += productS(element,depth + 1)
        else:
            sum+= element
    return sum
