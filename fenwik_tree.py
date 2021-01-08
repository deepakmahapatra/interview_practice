class IndexTree:
    def __init__(self, list_of_nums):
        self.bit_arr = [0] + list_of_nums
        for idx in range(1, len(self.bit_arr)):
            idx2 = idx + (idx & -idx)
            if idx2 < len(self.bit_arr):
                self.bit_arr[idx2] += self.bit_arr[idx]

    def prefix_sum(self, idx):
        idx += 1
        result = 0
        while idx:
            result += self.bit_arr[idx]
            idx -= (idx & -idx)
        return result

    def range_sum(self, idx1, idx2):
        return self.prefix_sum(idx2) - self.prefix_sum(idx1-1)

    def update(self, idx, val):
        idx += 1 # As we take the 0th element as dummy
        while idx < len(self.bit_arr):
            self.bit_arr[idx] += val
            idx += (idx & -idx)


if __name__ == '__main__':
    array = [1, 7, 3, 0, 5, 8, 3, 2, 6, 2, 1, 1, 4, 5]
    bit = IndexTree(array)
    print('Array: [{}]'.format(', '.join(map(str, array))))
    print()

    print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_sum(12)))
    print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_sum(6)))
    print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_sum(1, 5)))
    print()

    bit.update(4, 2)
    print('Add {} to element at pos {}'.format(2, 4))
    new_array = [bit.range_sum(idx, idx) for idx in range(len(array))]
    print('Array: [{}]'.format(', '.join(map(str, new_array))))
    print()

    print('Prefix sum of first {} elements: {}'.format(13, bit.prefix_sum(12)))
    print('Prefix sum of first {} elements: {}'.format(7, bit.prefix_sum(6)))
    print('Range sum from pos {} to pos {}: {}'.format(1, 5, bit.range_sum(1, 5)))
    print()

class SegementMaxTree:
    def __init__(self, list_):
        self.n = len(list_)
        self.array = [0] * self.n + list_
        for i in range(self.n, -1, 0):
            self.array[i] = max(self.array[2*i], self.array[2*i+1])

    def update(self, idx, val):
        idx += self.n
        self.array[idx] = val
        while idx >0:
            idx//=2
            self.array[idx] = max(self.array[2*idx], self.array[2*idx+1])

    def range_max(self, index1, index2):
        index1 += self.n
        index2 += self.n
        maxi = self.array[index1]
        while index1 < index2:
            if index1 %2:
                maxi = max(maxi, self.array[index1])
                index1+=1
            if index2 %2:
                index2 -=1
                maxi = max(maxi, self.array[index2])

            index2 //= 2
            index1 //= 2
        return maxi




