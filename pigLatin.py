def pigLatin(str):
    ''' Pig Latin takes the first consonant, moves it to the end of the word and
        place "ay" at the end.  If the strings starts with a vowel do nothing
        e.g. pig -> igpay, banana -> ananabay, egg -> egg
        '''

    vowels = 'aeiou'
    result = ''
    postfix = 'ay'
    try:
        if len(str) < 1:
            return result
        if str[0] in vowels:
            return str

        else:
            result = result + str[1:] + str[0] + postfix

        return result
    except Exception as e:
        print('You need to enter string.  Exception: {}'.format(e))


if __name__ == '__main__':
    print(pigLatin(23))
