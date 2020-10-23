"""
Problem:
- Given a 64-bit integer, reverse its digits.
Assumption:
- Negative numbers are also valid.
- Must handle the case where the reversed integer is overflow.
Example:
- Input: 123
  Output: 321
- Input: -123
  Output: -321
- Input: 8085774586302733229 Output: 0
  Explanation: The reversed integer 9223372036854775808 overflows by 1 so we return 0.
Approach:
- Use modulo by 10 to get a digit at ones' place of the input and
  dividing by 10 to shift it to the right (eliminate the ones' place).
Solution:
- Initialize the output as a 64-bit integer.
- If the input is not zero yet, keep multiply the output and diving the
  input by 10 so that: output = (output * 10) + (input % 10) and
  input = input / 10.
- Also, remember to check the overflow/underflow of the output and return
  0 if necessary.
Cost:
- O(m) time, O(1) space, where m is log10 of the input.
"""


def reverse_int(number):
    result = 0
    negative = False
    if number < 0:
        negative = True
        number = abs(number)

    while abs(number) > 0:
        if abs(result) > 8085774586302733229/10:
            return 0
        result = result * 10 + number % 10

        number = number//10
    if negative:
        return -result
    return result


if __name__ == "__main__":
    # print(reverse_int(123))
    print(reverse_int(-123))
    print(reverse_int(8085774586302733229))
    print(reverse_int(3287458723478))
