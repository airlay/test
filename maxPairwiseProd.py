def maxPairwiseProd(l):
    ans1 = 0
    ans2 = 0

    if len(l) < 2:
        return None
    if len(l) == 2:
        return list
    else:
        l.sort()
        x = l[len(l)-1] * l[-1]

        y = l[0] * l[1]

        if x > y:
            return l[-2:]
        else:
            return l[:2]


def maxPairwiseProd02(l):
    post1 =0
    post2 = 0
    neg1 = 0
    neg2 = 0

    for i in l:
        if i > post1:
            post2 = post1
            post1 = i
        else:
            post2 = i

        if i < 0 and i < neg1:
            neg2 = neg1
            neg1 = i
        elif i < 0 and i < neg2:
            neg2 = i

    print('negative numbers: {}, {}'.format(neg1, neg2))

    if neg1*neg2 > post1*post2:
        return print('{}, {}'.format(neg1, neg2))
    else:
        return print('{},{}'.format(post1, post2))


if __name__ == '__main__':

    l = [-1332, 9,6,7,8,23]
    print(maxPairwiseProd(l))



    # find both positive product and negative product



