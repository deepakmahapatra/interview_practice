def count_no_of_ways_to_climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_no_of_ways_to_climb_stairs(n-1) + count_no_of_ways_to_climb_stairs(n-2)


if __name__ == '__main__':
    print(count_no_of_ways_to_climb_stairs(5))
