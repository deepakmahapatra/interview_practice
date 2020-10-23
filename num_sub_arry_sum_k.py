

def sub_arr_sum_k(arr, summation):
    start = end = count = 0

    sum = arr[0]

    while start < len(arr) and end < len(arr):

        if sum < summation:
            end += 1

            if start <= end:
                count += end - start
            if end < len(arr):
                sum += arr[end]
        else:
            sum -=arr[start]
            start +=1
    return count




if __name__ == "__main__":
    # print(min_add_to_make_valid1("())))("))
    print(sub_arr_sum_k([-4,-2, 2 , 3], 4))