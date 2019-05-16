def bonetrousle(n, k, b):
    pass


def compareTriplets(a, b):
    apoints = 0
    bpoints = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            apoints += 1
        if b[i] > a[i]:
            bpoints += 1

    result = [apoints, bpoints]
    print('result type {}'.format(type(result)))
    return result


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(pos, neg, zero)
    print('{0:.6f}'.format(pos / len(arr)))
    print('{0:.6f}'.format(neg / len(arr)))
    print('{0:.6f}'.format(zero / len(arr)))


def staircase(n):
    for i in range(1,n+1):
        out = ''
        for j in range(n):
            if j < n-i:
                out = out + ' '
            else:
                out = out + '#'
        print(out)


def birthdayCakeCandles(ar):
    ar.sort()
    maxCandle = ar[-1]
    count = 0
    ar.reverse()
    for i in ar:
        if i == maxCandle:
            count += 1
    return count


def magicSquare(ar):

    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]



if __name__ == '__main__':
    # print(compareTriplets((5, 6, 7), (3, 6, 10)))
    # plusMinus([-4, 3, -9, 0, 4, 1])
    # staircase(10)

    birthdayCakeCandles([3, 2, 1, 3])