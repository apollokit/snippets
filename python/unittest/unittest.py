# see https://docs.python.org/3/library/unittest.html

import unittest

from text import TextWriter

wrtr = TextWriter()

class TestTextWriterBasics(unittest.TestCase):

    def test_closures(self):
        the_text = 'what the ` blah ( pineapple " baby ) word " uncle `'+\
            ' donkey ` well `'
        out = wrtr.fix_closures(the_text)
        out_expect = 'what the `blah(pineapple "baby)word" uncle` donkey `well`'
        self.assertEqual(out, out_expect)

if __name__ == '__main__':
    unittest.main()