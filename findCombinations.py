def findTotalcombo(arr, total):
    i = len(arr) - 1
    return recursive(arr, total, i)


def recursive(arr, total, index):
    # base case
    if total == 0:
        return 1
    elif total < 0:  # total is positive number . no negative number
        return 0
    elif index < 0:
        return 0
    # recursive case
    elif total < arr[index]:
        # if total (in sub array) is less than the current element, just skip and find the next one
        return recursive(arr, total, index - 1)
    else:
        # else calculate both number for total, and total-current element
        return recursive(arr, total - arr[index], index - 1) + recursive(arr, total, index - 1)


def findTotalcombo2(arr, total):
    return rec2(arr, total, len(arr) - 1)


def rec2(arr, total, i):
    # base case
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i <= 0:  # this means index is out of bound
        return 0
    elif total < arr[i]:
        return rec2(arr, total, i - 1)
    else:
        # print('index:element = {}:{}'.format(i, arr[i]))
        return rec2(arr, total, i - 1) + rec2(arr, total - arr[i], i - 1)


def findTotalcomboDP(arr, total):
    res = {}  # create a dictionory that can uniquely identify the set
    return recDP(arr, total, len(arr) - 1, res)


def recDP(arr, total, i, mem):
    # create key for mem, dynamic program
    key = str(total) + ':' + str(i)

    if key in mem:
        return mem[key]

    # base case
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    # elif total < arr[i]:
    #     subres = recDP(arr, total, i - 1, mem)
    else:
        subres = recDP(arr, total, i - 1, mem) + recDP(arr, total - arr[i], i - 1, mem)

    mem[key] = subres
    # print('key: subres = {} : {}'.format(key, subres))

    return subres


def subset(array, num):
    result = []
    path = ()

    def find(arr, num, path):
        if not arr:
            return
        if arr[0] == num:
            result.append(path + (arr[0],))
        else:
            find(arr[1:], num - arr[0], path + (arr[0],))
            find(arr[1:], num, path)

    find2(array, num, result, path)
    # find(array, num, path)
    return result


def find2(arr, num, result, path):

    if not arr:
        return None
    if arr[0] == num:
        result.append(path + (arr[0],))
    else:
        find2(arr[1:], num - arr[0], result, path + (arr[0],))
        find2(arr[1:], num, result, path)

    return result


def find2DP(arr, num, result, path, mem):

    key = path
    if mem[key] == num:
        return mem[key]

    if not arr:
        return None
    if arr[0] == num:
        result.append(path + (arr[0]))
        mem
    else:
        mem[key] = find2DP(arr, num, result, path + (arr[0]))
        mem[key] = find2DP(arr, num-arr[0], result, path)
    return mem[key]

if __name__ == '__main__':
    mylist = [1, 2, 3,4,5,4, 6, 10, 16]
    print(subset(mylist, 16))

    print(findTotalcomboDP(mylist, 32))