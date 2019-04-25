import string


def isAnagram(a, b):
    # result = False

    # strip off all spaces and puncuations
    try:
        translater = str.maketrans('', '', string.punctuation)

        a = a.translate(translater).lower()
        b = b.translate(translater).lower()

        asorted = sorted(a)
        bsorted = sorted(b)

        if asorted == bsorted:
            return True
        else:
            return False
    except AttributeError:
        print('damn...please input string only')


if __name__ == '__main__':
    print(isAnagram('army', 1234))
