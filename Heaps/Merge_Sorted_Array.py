import Heap


def mergeSortedArrays(arrays):
    sorted_array = []

    array_pointers = [0 for array in arrays]

    min_heap = Heap.Heap([], comparison_func)

    for i in range(len(arrays)):
        min_heap.insert([i, arrays[i][0]])

    while not min_heap.is_empty():
        next_sorted_element = min_heap.remove()
        sorted_array.append(next_sorted_element[1])
        array_of_next_element_idx = next_sorted_element[0]
        array_pointers[array_of_next_element_idx] += 1

        if array_pointers[array_of_next_element_idx] == len(arrays[array_of_next_element_idx]):
            continue
        min_heap.insert([array_of_next_element_idx,arrays[array_of_next_element_idx][array_pointers[array_of_next_element_idx]]])

    return sorted_array


def comparison_func(a, b):
    return a[1] < b[1]


