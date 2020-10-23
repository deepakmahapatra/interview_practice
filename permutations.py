if __name__ == '__main__':
    def permutations(input, left, right):
        if left == right:
            print(''.join(input))
        else:
            for i in range(left, right+1):
                input[left], input[i] = input[i], input[left]
                permutations(input, left+1, right)
                input[left], input[i]= input[i], input[left]

    permutations(["a","b","c"],0,2)
