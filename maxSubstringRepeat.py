def maxsubstringrepeat(inputstring):
    longest = 0
    dic = {}
    startpoint = 0
    for i in range(len(inputstring)):
        if inputstring[i] not in dic:
            dic[inputstring[i]] = i
            longest = i - startpoint +1

        else:  # possible repeatition detected
            if dic[inputstring[i]] < startpoint:  #  check if current letter is inside the current string
                longest += 1
                dic[inputstring[i]] = i
            else:  # repeated letter detected
                cursubtstring = i - dic[inputstring[i]]
                longest = max(longest, cursubtstring)
                startpoint = dic[inputstring[i]] +1
                dic[inputstring[i]] = i

    return longest


if __name__ == '__main__':
    s = 'abdbfgabefsdfadfjadfqwertyuiop'
    print(maxsubstringrepeat(s))

