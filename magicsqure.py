import datetime

def formingMagicSquare(s):
    magicsquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    totals = []

    for p in magicsquares:
        total = 0

        for p_row, s_row in zip(p, s):
            print('##################')
            for i, j in zip(p_row, s_row):
                if i != j:
                    print('i:{}, j:{}'.format(i, j))
                    print('abs(i-j):{}'.format(abs(i - j)))
                    total += abs(i - j)
                    # print('total: {}'.format(total))
        totals.append(total)

    print(totals)
    return min(totals)


def pickingNumbers(a):
    # put in a map
    dic = {}
    for i in a:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1

    l = []
    for i in dic.keys():
        l.append(i)

    l.sort()
    pre = 0
    result = 0  # dic[l[pre]]

    if len(l) == 1:
        return dic[l[0]]

    for i in range(1, len(l) - 1):

        # print('###################')
        # print('i :{}, l[i]:{}'.format(i, l[i]))
        if l[pre] + 1 == l[i]:  # in sequence
            # print('count:{}, result = {}'.format(count, result))
            result = max(dic[l[i]] + dic[l[pre]], result)
            pre = i

            # count = dic[l[i]]  # reset count
        else:  # diff > 1
            # print('in else pre:{}'.format(pre))
            # print('l[pre]: {}'.format(l[pre]))
            count = dic[l[pre]]
            result = max(count, dic[l[i]], result)
            pre = i

    result = max(result, dic[l[i]])

    # print('result:{}'.format(result))
    return result


def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)

    # print('scores: {}'.format(scores))
    # print('alice: {}'.format(alice))
    alicerank = []
    l = len(scores)
    for a in alice:
        while (l > 0) and (a >= scores[l - 1]):
            l -= 1
        alicerank.append(l + 1)

    return alicerank


def designerPdfViewer(h, word):
    maxheight = 0

    for i in word:
        maxheight = max(maxheight, (h[ord(i) - 97]))

    return maxheight * len(word)


def angryProfessor(k, a):
    ontime = 0

    for i in a:
        if i >= 0:
            ontime += 1
    if ontime >= k:
        return 'YES'
    else:
        return 'NO'


def beautifulDays(i, j, k):
    beautifulday = 0
    while i <= j:
        reverse = int(str(i)[::-1])
        print('reverse :{}'.format(reverse))
        print(abs(i - reverse) % k)

        if (abs(i - reverse) % k == 0):
            beautifulday += 1
        i += 1
    return beautifulday


def viralAdvertising(n):
    people = 5
    accu = 0

    for i in range(1, n + 1):
        like = people // 2
        people = (people // 2) * 3
        accu += like
    return accu


def saveThePrisoner(n, m, s):
    badsweet = ((m + s - 1) % n)

    if badsweet == 0:
        return n

    else:
        return badsweet


def circularArrayRotation(a, k, queries):
    for i in range(k - 1):
        p = a.pop(0)
        a.append(p)
    for i in queries:
        print(a[i])


def permutationEquation(p):
    result = []
    print('p:{}'.format(p))
    for i in range(1, len(p) + 1):
        x = p.index(i) + 1
        print('x:{}, y:{}'.format(x, p.index(x) + 1))

        result.append(p.index(x) + 1)

    return result


def jumpingOnClouds(c, k):
    # i = 0
    print('K:{}'.format(k))
    print('len(c):{}'.format(len(c)))
    energy = 100  # - 2*c[0]
    for i in c[::k]:
        print('jump :{}'.format(i))
        energy = energy - (1 + (2 * i))

    return energy


def findDigits(n):
    s = str(n)
    total = 0
    for i in s:
        if int(i) != 0:
            if n % int(i) == 0:
                total += 1
    return total


def extraLongFactorials(n):
    # fact= [0]*(n+1)
    #
    # fact[0] = 1
    # fact[1] =1
    # for i in range(2, n+1):
    #     fact[i] = i*fact[i-1]
    result = 1
    for i in range(1, n + 1):
        result = i * result

    return result  # fact[n]


def appendAndDelete(s, t, k):
    i = 0

    if len(s) + len(t) <= k:
        return True


    # find the prefix
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1

    # print('i : {}'.format(i))

    # characters need to update
    charupdates = len(s[i:]) + len(t[i:])
    if charupdates <= k and (k - charupdates) % 2 == 0:
        return True

    else:
        return False


def squares(a, b):
    i = 1
    total = 0
    while (i*i) <= b:
        if i*i >= a:
            total +=1
        i += 1

    print(total)

    return total

def libraryFine(d1, m1, y1, d2, m2, y2):
    indate1 = str(d1)+str(m1)+str(y1)
    indate2 = str(d2)+str(m2)+str(y2)
    expireddate = datetime.date(indate1, '%d%m%d')
    #s_datetime = datetime.datetime.strptime(s, '%Y%m%d')


if __name__ == '__main__':
    squares(3, 9)

    # s = 'abc' # 'hackerhappy'
    # t = 'abc' # 'hackerrank'
    # print(appendAndDelete(s, t, 5))
    # print(extraLongFactorials(25))
    # c = [0, 0, 1, 0, 0, 1, 1, 0]
    # c2 = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    # k = 2
    # k2 = 3
    # print(jumpingOnClouds(c, k))

    # t = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
    # t2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    # t22 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
    # print(formingMagicSquare(t22))

    # l = [4, 6, 5, 3, 3, 1]
    # l2 = [1, 2, 2, 3, 1, 2]
    # l3 = [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5,
    #       97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4,
    #       97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97,
    #       5, 97, 5, 97, 97, 97]
    #
    # l4 = [55, 55, 55, 55, 55]
    # pickingNumbers(l4)
    #
    # scores = [100, 90, 90, 80, 75, 60]
    # tscore0 = [100, 90, 90, 80, 75, 60]
    # alice0 = [50, 65, 77, 90, 102]
    # alice = [50, 65, 77, 90, 102]
    #
    # tscore1 = [100, 100, 50, 40, 40, 20, 10]
    # alice1 = [5, 25, 50, 120]
    #
    # result = climbingLeaderboard(scores, alice)
    #
    # print(result)
    #

    # h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    # word = 'abc'
    # designerPdfViewer(h, word)
    # a = [-1, -3, 4, 2]
    # print(angryProfessor(3, a))

    # print(beautifulDays(20, 23, 6))

    # for i in range(1,2):
    #     print('i:{} => {}'.format(i, viralAdvertising(i)))

    # print(saveThePrisoner(3,7,3))
    # print(saveThePrisoner(7, 19, 2))
    # print(saveThePrisoner(999999998, 999999997, 1))
    #

    # circularArrayRotation([1,2,3], 2, [0,1,2])
    # p1 = [2,3,1]
    # p = [4, 3, 5, 1, 2]
    # print(permutationEquation(p))
