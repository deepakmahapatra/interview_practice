if __name__ == '__main__':
    def permutations(input, left, right, result):
        if left == right:
            result.append(''.join(input))
        else:
            for i in range(left, right+1):
                input[left], input[i] = input[i], input[left]
                permutations(input, left+1, right, result)
                input[left], input[i] = input[i], input[left]
    result = list()
    permutations(["a", "b", "c"], 0, 2, result)
    for i in result:
        print(i)
