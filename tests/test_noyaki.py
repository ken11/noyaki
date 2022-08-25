import os
import sys
import unittest
sys.path.append(os.path.abspath("./src"))
from noyaki import noyaki


class TestNoyaki(unittest.TestCase):

    def test_convert_u(self):
        label_list = noyaki.convert(
            ['明日', 'は', '田中', 'さん', 'に', '会う'],
            [[3, 5, 'PERSON']]
        )
        self.assertEqual(label_list, ['O', 'O', 'U-PERSON', 'O', 'O', 'O'])

    def test_convert_bl(self):
        label_list = noyaki.convert(
            ['明日', 'は', '田中', '太郎', 'さん', 'に', '会う'],
            [[3, 7, 'PERSON']]
        )
        self.assertEqual(label_list, ['O', 'O', 'B-PERSON', 'L-PERSON', 'O', 'O', 'O'])

    def test_convert_bil(self):
        label_list = noyaki.convert(
            ['明日', 'は', '田中', 'ジェームス', '太郎', 'さん', 'に', '会う'],
            [[3, 12, 'PERSON']]
        )
        self.assertEqual(label_list, ['O', 'O', 'B-PERSON', 'I-PERSON', 'L-PERSON', 'O', 'O', 'O'])

    def test_convert_b(self):
        label_list = noyaki.convert(
            ['明日', 'は', '田中', 'さん', 'に', '会う'],
            [[3, 5, 'PERSON']],
            scheme="IOB2"
        )
        self.assertEqual(label_list, ['O', 'O', 'B-PERSON', 'O', 'O', 'O'])

    def test_convert_bi(self):
        label_list = noyaki.convert(
            ['明日', 'は', '田中', '太郎', 'さん', 'に', '会う'],
            [[3, 7, 'PERSON']],
            scheme="IOB2"
        )
        self.assertEqual(label_list, ['O', 'O', 'B-PERSON', 'I-PERSON', 'O', 'O', 'O'])

    def test_convert_bii(self):
        label_list = noyaki.convert(
            ['明日', 'は', '田中', 'ジェームス', '太郎', 'さん', 'に', '会う'],
            [[3, 12, 'PERSON']],
            scheme="IOB2"
        )
        self.assertEqual(label_list, ['O', 'O', 'B-PERSON', 'I-PERSON', 'I-PERSON', 'O', 'O', 'O'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
