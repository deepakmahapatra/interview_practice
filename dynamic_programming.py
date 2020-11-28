def count_no_of_ways_to_climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_no_of_ways_to_climb_stairs(n-1) + count_no_of_ways_to_climb_stairs(n-2)


def count_no_of_ways_to_climb(n):
    s = []
    s.append(0)
    s.append(1)
    s.append(2)
    for i in range(3, n+1):
        s.append(s[i-1]+s[i-2])
    return s[n]


if __name__ == '__main__':
    print(count_no_of_ways_to_climb_stairs(5))
    print(count_no_of_ways_to_climb(5))
