def findOnes(arr):
    ''' input: [0...0,1...1] a string that starts with either 0 or 1, but never end with 0 after 1
        output: total 1's or zero
        e.g. [000111] -> 3, [000] -> 0, [1111] -> 4
    '''

    start = 0
    end = len(arr) - 1

    if arr[end] == 0:
        return 0
    if arr[0] == 1:
        return len(arr)

    while start < end:
        mid = (start + end) // 2
        print('mid: {}'.format(mid))
        if arr[mid] == 0:  # leftside of arr[0] has no 1, ignore
            start = mid
        else:  # arr[mid] is 1 need to check if the left element is 0 or 1
            if arr[mid - 1] == 1:  # right side of arr are 1's need to search left side
                end = mid
            else:
                break

    result = len(arr) - mid
    print('here :{}'.format(result))
    return result


if __name__ == '__main__':
    input = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, ]

    print(findOnes(input))
