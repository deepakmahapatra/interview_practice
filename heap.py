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
        return self.count == self.maxsize

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def shift_up(self, index):
        pass

    def shift_down(self, index):
        pass


class MinHeap(BaseHeap):
    def __init__(self, maxsize, compare=None):
        super(MinHeap, self).__init__(maxsize)
        if compare:
            self.compare = compare
        else:
            self.compare = lambda x, y: True if x < y else False

    def shift_down(self, index):
        left_index = self.get_left_index(index)
        right_index = self.get_right_index(index)

        smaller_index = -1

        if left_index != -1 and right_index != -1:
            smaller_index = left_index if self.compare(self.heap[left_index], self.heap[right_index]) else right_index
        elif left_index != -1:
            smaller_index = left_index
        elif right_index != -1:
            smaller_index = left_index

        if smaller_index == -1:
            return
        if self.compare(self.heap[smaller_index], self.heap[index]):
            self.swap(smaller_index, index)
            self.shift_down(smaller_index)

    def shift_up(self, index):
        parent_index = self.get_parent_index(index)
        if parent_index != -1 and not self.compare(self.heap[parent_index], self.heap[index]):
            self.swap(parent_index, index)
            self.shift_up(parent_index)

    def insert(self, node):
        if self.count == self.maxsize:
            raise Exception
        self.heap.append(node)
        self.count = len(self.heap)
        self.shift_up(self.count-1)
        self.shift_down(0)

    def delete_head(self):
        self.swap(0, self.count-1)
        self.heap.pop()
        self.count -= 1
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


class MaxHeap(BaseHeap):
    def __init__(self, maxsize, compare=None):
        super( MaxHeap, self).__init__(maxsize)
        if compare:
            self.compare = compare
        else:
            self.compare = lambda x, y: True if x > y else False

    def shift_down(self, index):
        left_index = self.get_left_index(index)
        right_index = self.get_right_index(index)

        smaller_index = -1

        if left_index != -1 and right_index != -1:
            smaller_index = left_index if self.compare(self.heap[left_index], self.heap[right_index]) else right_index
        elif left_index != -1:
            smaller_index = left_index
        elif right_index != -1:
            smaller_index = left_index

        if smaller_index == -1:
            return
        if self.compare(self.heap[smaller_index], self.heap[index]):
            self.swap(smaller_index, index)
            self.shift_down(smaller_index)

    def shift_up(self, index):
        parent_index = self.get_parent_index(index)
        if parent_index != -1 and not self.compare(self.heap[parent_index], self.heap[index]):
            self.swap(parent_index, index)
            self.shift_up(parent_index)

    def insert(self, node):
        if self.count == self.maxsize:
            raise Exception
        self.heap.append(node)
        self.count = len(self.heap)
        self.shift_up(self.count-1)
        self.shift_down(0)

    def delete_head(self):
        self.swap(0, self.count-1)
        self.heap.pop()
        self.count -= 1
        self.shift_down(0)

    def find_min_in_maxheap(self):
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
            if max_element > self.heap[i]:
                max_element = self.heap[i]
        return max_element


def find_largest_in_stream(stream, k):
    """
    use a min heap with size k to store elements as they come in
    :return:
    """
    heap = MinHeap(k)
    result_list = []
    for i in stream:
        if heap.is_empty():
            heap.insert(i)
        elif heap.get_highest_priority() < i:
            if heap.is_full():
                heap.delete_head()
            heap.insert(i)
    while heap.count != 0:
        result_list.append(heap.get_highest_priority())
        heap.delete_head()
    return result_list


def merge_k_sorted_array(input, total_items):
    class Node:
        def __init__(self, data, list_index):
            self.data = data
            self.list_index = list_index
    result = list()

    def compare(left, right):
        return left.data < right.data

    heap = MinHeap(len(input), compare)
    for index, list_itmes in enumerate(input):
        heap.insert(Node(list_itmes.pop(0), index))

    while len(result) < total_items:
        element = heap.get_highest_priority()
        heap.delete_head()
        result.append(element.data)
        if input[element.list_index]:
            heap.insert(Node(input[element.list_index].pop(0), element.list_index))
    return result


def median_of_stream(input, min_heap, max_heap):
    if (not max_heap.is_empty()) and input > max_heap.get_highest_priority():
        min_heap.insert(input)
    else:
        max_heap.insert(input)

    if (max_heap.count - min_heap.count) > 1:
        min_heap.insert(max_heap.get_highest_priority())
        max_heap.delete_head()
    elif (min_heap.count - max_heap.count) > 1:
        max_heap.insert(min_heap.get_highest_priority())
        min_heap.delete_head()
    if min_heap.count == max_heap.count:
        return (min_heap.get_highest_priority() + max_heap.get_highest_priority())/2.0
    return min_heap.get_highest_priority() if min_heap.count > max_heap.count else max_heap.get_highest_priority()


if __name__ == '__main__':
    lists = [[1, 2], [3, 4, 5], [3, 9, 12]]
    result = merge_k_sorted_array(lists, 8)
    result2 = find_largest_in_stream([1, 2, 3, 22, 3, 5, 6, 1, 33], 3)
    min_heap = MinHeap(float('inf'))
    max_heap = MaxHeap(float('inf'))
    for i in [1, 2, 3, 22, 4, 5, 6, 1]:
        result3 = median_of_stream(i, min_heap, max_heap)
    print(result3)
    print(result)
    print(result2)




