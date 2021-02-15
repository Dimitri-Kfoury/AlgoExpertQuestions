def shortenPath(path):
    stack = []
    path = path.split('/')

    if path[0] == '':
        for i in range(1, len(path)):
            if path[i] == '..':
                if len(stack):
                    stack.pop()
            elif path[i] == '' or path[i] == '.':
                continue
            else:
                stack.append(path[i])
        return '/' + reconstruct_path(stack) if len(stack) else ''
    else:
        i = 0
        while path[i] == '..':
            stack.append(path[i])
            i += 1
        for i in range(i, len(path)):
            if path[i] == '..' and len(stack) and stack[-1] != '..':
                stack.pop()
            elif path[i] == '' or path[i] == '.':
                continue
            else:
                stack.append(path[i])
        return reconstruct_path(stack) if len(stack) else ''


def reconstruct_path(stack):
    path = stack[0]
    for i in range(1, len(stack)):
        path += '/' + stack[i]
    return path

