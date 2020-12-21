from collections import defaultdict


def prefix(A):
    """
    Find shortest unique prefix to represent each word in the list.

    Example:

    Input: [zebra, dog, duck, dove]
    Output: {z, dog, du, dov}
    where we can see that
    zebra = z
    dog = dog
    duck = du
    dove = dov
    """

    prefixes = defaultdict(int)
    for word in A:
        for i in range(len(word)):
            prefixes[word[:i]] += 1
    res = []
    for word in A:
        rest = word
        for i in range(len(word)):
            if prefixes[word[:i]] == 1:
                rest = word[:i]
                break
        res.append(rest)
    return res
