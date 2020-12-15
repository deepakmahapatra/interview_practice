from collections import deque


def slidingMaximum(A, B):
    dq = deque()
    result = []
    for i in range(len(A)):
        while dq and A[i] > A[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= B and dq and dq[0] == i - B:
            dq.popleft()
        if i >= B - 1:
            result.append(A[dq[0]])
    return result



if __name__ == '__main__':
    slidingMaximum([10,9,10,11,6], 3)