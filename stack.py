def isValid(s: str) -> bool:
    """
    given a string s check if it is a valid parantheses combination or not
    :param self:
    :param s:
    :return:
    """
    stack = []
    dict_paran = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    for i in s:
        if i in '({[':
            stack.append(i)
        else:
            if not stack:
                return False
            if stack and dict_paran[stack.pop()] != i:
                return False
    if not stack:
        return True
    return False

