# How to Print duplicate characters from String
def findDupliateCharacters(inputstring):
    # preconditions: iput string can be empty, can have no duplicate
    # output: characters that occurs more than once
    # e.g. "java" -> a=2, python -> no
    # solution put the characters in dictionary, and add the value if there is duplicate

    result = {}
    resultstring =''
    try:
        for i in inputstring:
            if i not in result:
                result[i] = 1
            else:
                result[i] = result[i]+1
        # print(result)
        for k,val in result.items():
            if val > 1:
                resultstring = resultstring + k

    except TypeError:
        print('Damn....you\'ve got type error')

    # print(resultstring)
    return resultstring


def find_none_duplicate_char(inputsting):
    result = {}
    try:
        for i in inputsting:
            if i not in result:
                result[i] = 1
            else:
                result[i] = result[i]+1

        for k,val in result.items():
            if val == 1:
                return k

        return None

    except TypeError:
        print('Please use sting')


# if __name__ == '__main__':
#     # r = findDupliateCharacters('java')
#     # s = findDupliateCharacters('aabbcc')
#
#     a = find_none_duplicate_char('java')
#     print(a)


