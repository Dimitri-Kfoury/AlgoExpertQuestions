def diskStacking(disks):

    disks.sort(key = lambda disk : disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0,i):
            otherDisk = disks[j]
            if areValidDimensions(currentDisk,otherDisk):
                if heights[i] <= currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxIdx]:
            maxIdx = i
    return buildSequence(sequences,disks,maxIdx)


def areValidDimensions(disk,otherDisk):
    return otherDisk[0] < disk[0] and otherDisk[1] < disk[1] and otherDisk[2] < disk[2]

def buildSequence(sequences,disks,maxIdx):
    sequence = []
    i = maxIdx
    while sequence[i] is not None:
        sequence.append(disks[i])
        i = sequence[i]
    return sequence




