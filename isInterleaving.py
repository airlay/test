def isInterleaving(str1, str2, str3):
    ''' str3 is interleaving of str1 and str2 if it can be form by interleaving the characters of str1 and str2 in a way
    that maintains the left to right order of the characters from each string

    e.g. aabx, bbax, aabbxax -> true, aabx, bbax, axabbbx -> false
    '''

    str1len = len(str1)
    str2len = len(str2)
    str3len = len(str3)

    # if str3 is not sum of str1 and str2, False
    if str1len + str2len != str3len:
        return False
    # if all strings are empty, return True
    if str1len == str2len == str3len == 0:
        return True

    i = 0
    j = 0
    k = 0

    while k < str3len:
        if str3[k] == str1[i]:  # check against first string
            i += 1
        elif str3[k] == str2[j]:  # check against second string
            j += 1
        else:  # none of them match
            return False
        k += 1

    if i == str1len and j == str2len and k == str3len:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isInterleaving('XXYM', 'XXZT', 'XXXZXYTM'))