class MaxHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def build_heap(self, array):

        end_idx = len(array) - 1
        for i in range((len(array) - 2) // 2, -1, -1):
            self.sift_down(i, end_idx, array)
        return array

    def sift_down(self, start_idx, end_idx, heap):

        current_idx = start_idx
        left_child_idx = 2 * current_idx + 1
        while left_child_idx <= end_idx:

            right_child_idx = 2 * current_idx + 2 if 2 * current_idx + 2 <= end_idx else -1

            if right_child_idx != -1 and heap[right_child_idx] > heap[left_child_idx]:
                max_child_idx = right_child_idx
            else:
                max_child_idx = left_child_idx

            if heap[max_child_idx] > heap[current_idx]:
                self.swap(heap,max_child_idx, current_idx)
                current_idx = max_child_idx
                left_child_idx = 2 * current_idx + 1
            else:
                return

    def sift_up(self, start_idx, heap):

        current_idx = start_idx
        parent_idx = (current_idx - 1) // 2
        while parent_idx >= 0 and heap[parent_idx] < heap[current_idx]:
            self.swap(heap, parent_idx, current_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def remove(self):
        final_idx = len(self.heap) - 1
        self.swap(self.heap, 0, final_idx)
        removed_value = self.heap.pop()
        self.sift_down(0, final_idx, self.heap)
        return removed_value

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]
