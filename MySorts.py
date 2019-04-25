def bubblesort(list):
    for item_num in range(len(list) - 1, 0, -1):
        for ind in range(item_num):
            if list[ind] > list[ind + 1]:
                temp = list[ind]
                list[ind] = list[ind + 1]
                list[ind + 1] = temp


def merge_sort(list):
    if len(list) <= 1:
        return list

    middlepoint = len(list) // 2
    leftlist = list[:middlepoint]
    rightlist = list[middlepoint:]

    leftlist = (leftlist)
    rightlist = (rightlist)
    return merge(leftlist, rightlist)


def merge(llist, rlist):
    result = []

    # compare left and right list and put the lesser one into result[]
    while len(llist) != 0 and len(rlist) != 0:
        if llist[0] < rlist[0]:
            result.append(llist[0])
            llist.remove(llist[0])
        else:
            result.append(rlist[0])
            rlist.remove(rlist[0])
    # join extra elements in any left or right list if any
    if len(llist) > 0:
        result + llist
    else:
        result + rlist

    return result


def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        # print(InputList[i])
        j = i - 1
        next_element = InputList[i]

        while (InputList[j] > next_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j = j - 1
        InputList[j + 1] = next_element


def shell_sort(inputlist):
    gap = len(inputlist)//2

    while gap > 0:

        for i in range(gap, len(inputlist)):
            temp = inputlist[i]
            j = i
            while j >= gap and inputlist[j-gap] > temp:
                inputlist[j] = inputlist[j-gap]
                j = j-gap
            inputlist[j] = temp

        gap = gap // 2

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# print(merge_sort(unsorted_list))

#
# l = [19, 2, 31, 45, 6, 11, 121, 27]
# print(l)
# print('============')
# print(shell_sort(l))
# print(l)


def sorted_binary_search(list, value):
    # prereq: list must be sored
    mid_point = len(list)//2
    # base cases
    print(list[mid_point])
    if value == list[mid_point]:
        print('found {} at index[{}]'.format(value, mid_point))
        return True
    elif value > list[mid_point]:
        return sorted_binary_search(list[mid_point: len(list)], value)
    elif value < list[mid_point]:
        return sorted_binary_search(list[:mid_point], value)
    else:
        return False


m = [2, 6, 11, 19, 27, 31, 45, 121]
print(sorted_binary_search(m, 2))