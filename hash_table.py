import collections
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

def minDeletions(s: str) -> int:
    """
    given a string s make the frequencies of the characters unique by deleting minimum number of elements
    Args:
        s:

    Returns:

    """
    freq = collections.defaultdict(int)
    count = 0
    for item in s:
        freq[item] += 1
    unique_freq = set()
    for key, curr_count in freq.items():
        while curr_count in unique_freq and curr_count > 0:
            curr_count -= 1
            count += 1
        unique_freq.add(curr_count)
    return count