def findAndReplacePattern(words, pattern):
    """
    ou have a list of words and a pattern, and you want to know which words in words matches the pattern.

    A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

    (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

    Return a list of the words in words that match the given pattern.

    You may return the answer in any order.
    :param self:
    :param words:
    :param pattern:
    :return:
    """
    def helper_indexer(word):
       dict_ = {}
       return [dict_.setdefault(c, len(dict_)) for c in word]
    inde_p = helper_indexer(pattern)
    return [word for word in words if helper_indexer(word) == inde_p]


if __name__ == '__main__':
    print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
    print(findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))