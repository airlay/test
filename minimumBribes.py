def minimumBribes(q):
    # Any person in the queue can bribe the person directly in front of them to swap positions.
    # If two people swap positions, they still wear the same sticker denoting their original places in line. One person
    # can bribe at most two others. For example, if n=8 and person 5 bribes person4 , the queue will look like this:
    # 1,2,3,5,4,6,7,8.

    bribes = 0
    for i, p in enumerate(q):
        if (p - 1) - i > 2:
            print('Too chaotic')
            return
        print('i: {}'.format(i))
        for j in range(max(0, p - 2), i):
            print('j: {}, p-2 : {}'.format(j, p - 2))
            if q[j] > p:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    arr2 = [2, 5, 1, 3, 4]
    arr = [2, 1, 5, 3, 4]
    arr3 = [2, 1, 5, 6, 3, 4, 9, 8, 11, 7, 10, 14, 13, 12, 17, 16, 15, 19, 18, 22, 20, 24, 23, 21, 27, 28, 25, 26, 30,
            29]
    minimumBribes(arr)
    minimumBribes(arr3)
