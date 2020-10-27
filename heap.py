class BaseHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.heap = list()
        self.count = 0

    def get_left_index(self, index):
        return 2*index + 1 if 2*index + 1 < self.count else -1

    def get_right_index(self, index):
        return 2*index + 2 if 2*index + 2 < self.count else -1

    def get_parent_index(self, index):
        return (index-1)//2 if self.count > (index-1)//2 > 0 else -1

    def get_highest_priority(self):
        if self.count == 0:
            raise Exception
        return self.heap[0]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.heap)

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def shift_up(self, index):
        pass

    def shift_down(self, index):
        pass


class MinHeap(BaseHeap):
    def __init__(self, maxsize):
        super(MinHeap, self).__init__(maxsize)

    def shift_down(self, index):
        left_index = self.get_left_index(index)
        right_index = self.get_right_index(index)

        smaller_index = -1

        if left_index != -1 and right_index != -1:
            smaller_index = self.heap[left_index] if self.heap[left_index] < self.heap[right_index] else self.heap[right_index]
        elif left_index != -1:
            smaller_index = left_index
        elif right_index != -1:
            smaller_index = left_index

        if smaller_index == -1:
            return
        if self.heap[smaller_index] < self.heap[index]:
            self.swap(smaller_index, index)
            self.shift_down(smaller_index)

    def shift_up(self, index):
        parent_index = self.get_parent_index(index)
        if parent_index != -1 and self.heap[parent_index] > self.heap[index]:
            self.swap(parent_index, index)
            self.shift_up(parent_index)

    def insert(self, node):
        if self.count == len(self.heap):
            raise Exception
        self.heap.append(node)
        self.count = len(self.heap)
        self.shift_up(self.count-1)
        self.shift_down(0)

    def delete_head(self):
        self.swap(0, self.count-1)
        self.heap.pop()
        self.shift_down(0)

    def find_max_in_minheap(self):
        """
        One of the leaf nodes has to be maximum
        find the first leaf node, see contiguous elements
        the first leaf comes after the last internal node
        :return:
        """
        last_index = self.count - 1
        last_parent_index = self.get_parent_index(last_index)

        first_child_index = last_parent_index + 1

        max_element = self.heap[first_child_index]

        for i in range(first_child_index,last_index+1):
            if max_element < self.heap[i]:
                max_element = self.heap[i]
        return max_element

def find_largest_in_stream(stream , k):
    """
    use a min heap with size k to store elements as they come in
    :return:
    """
    heap = MinHeap(k)
    for i in stream:
        if heap.is_empty():
            heap.insert(i)
        elif heap.get_highest_priority() < i:
            if heap.is_full():
                heap.delete_head()
            heap.insert(i)




