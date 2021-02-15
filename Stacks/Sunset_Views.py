def sunsetViews(buildings, direction):

    stack = []

    if direction == 'EAST':
        for i  in range(len(buildings)):
            while len(stack) > 0 and buildings[i] >= buildings[stack[len(stack) - 1]]:
                stack.pop()
            stack.append(i)

    if direction == 'WEST':
        for i in range(len(buildings)-1,-1,-1):
            while len(stack) > 0 and buildings[i] >= buildings[stack[len(stack) - 1]]:
                stack.pop()
            stack.append(i)
        stack = list(reversed(stack))

    return stack

