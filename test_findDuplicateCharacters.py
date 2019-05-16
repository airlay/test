import unittest
from findDuplicateCharacters import findDupliateCharacters
from findDuplicateCharacters import find_none_duplicate_char
from Isanagram import isAnagram


class TestFindDupChar(unittest.TestCase):
    def testOneDuplicate(self):
        self.assertEqual(findDupliateCharacters('java'), 'a')
        # self.assertEqual(findDupliateCharacters(None), '')
        self.assertEqual(findDupliateCharacters('asdf'), '')
        self.assertEqual(findDupliateCharacters('aabbcc'), 'abc')
        # self.assertEqual(findDupliateCharacters(34), 'Oops....we\'ve got type error')
        self.assertEqual(findDupliateCharacters(34), None)

    def test_is_agnagram(self):
        self.assertEqual(isAnagram('army', 'mary'), True)
        self.assertEqual(isAnagram('adf', 'adsfadfa'), False)

    def test_first_none_repeated_char(self):
        self.assertEqual(find_none_duplicate_char('java'), 'j')
        self.assertEqual(find_none_duplicate_char('aaddbbbccxs'), 'x')
        self.assertEqual(find_none_duplicate_char('aabbccddeeffl'), 'l')
        self.assertEqual(find_none_duplicate_char('aabbcc'), None)


if __name__ == '__main__':
    import xmlrunner

    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_findDub-reports'))
