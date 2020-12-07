def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    max_len = 0
    dict_ = {}
    if not s:
        return 0
    for idx in range(len(s)):
        if s[idx] in dict_:
            start = max(start, dict_[s[idx]] + 1)
        dict_[s[idx]] = idx
        max_len = max(max_len, idx - start + 1)
    return max_len