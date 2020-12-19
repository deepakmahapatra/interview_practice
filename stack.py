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


def decode_string(string_):
    stack = []
    curr_str = ''
    curr_num = 0
    for i in string_:
        if i == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ''
            curr_num = 0
        elif i == ']':
            num = stack.pop()
            char = stack.pop()
            curr_str = char + num * curr_str
        elif i.isdigit():
            curr_num = curr_num * 10 + int(i)
        else:
            curr_str += i
    return curr_str


def first_non_repeating_char(A):
    """
    Given a string A denoting a stream of lowercase alphabets. You have to make new string B.

    B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.



    Problem Constraints
    1 <= length of the string <= 100000



    Input Format
    The only argument given is string A.



    Output Format
    Return a string B after processing the stream of lowercase alphabets A.



    Example Input
    Input 1:

     A = "abadbc"
    Input 2:

     A = "abcabc"


    Example Output
    Output 1:

     "aabbdd"
    Output 2:

     "aaabc#"


    :param self:
    :param A:
    :return:
    """
    queue = []
    repeated = set()
    visited = set()
    res = []
    for elem in A:
        if elem not in visited:
            visited.add(elem)
            queue.append(elem)
        elif elem not in repeated:
            repeated.add(elem)
            queue.remove(elem)
        res.append(queue[0] if queue else '#')
    return ''.join(res)


if __name__ == '__main__':
    print(first_non_repeating_char("aabb"))