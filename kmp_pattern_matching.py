def build_lps(patterns):
    lps = [0] * len(patterns)
    length = i = 0
    while i < len(patterns):
        if patterns[i] == patterns[length]:
            lps[i] = length
            i+=1
        else:
            if length != 0:
                lps[i] = lps[i-1]
            else:
                lps[i] = 0
                i += 1
    print(lps)
    return lps

def pattern_match(text, pattern):
    m = len(text)
    n = len(pattern)

    i = j = 0
    lps = build_lps(pattern)
    res = []
    while i < m:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == n:
            res.append(i-j)
            j = lps[j-1]
        elif i < m and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
    return res
if __name__ == '__main__':
    pattern = "abcabc"
    text = "adefabcabdabcabckghdkabfabcabc"
    print(pattern_match(text, pattern))