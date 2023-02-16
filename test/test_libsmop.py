from smop.lib import *
import unittest


class test_libsmop(unittest.TestCase):
    def test_diff(self):
        a = matlabarray([[1, 2, 3], [4, 5, 6]])
        b = diff(a)
        print(b)
        self.assertTrue(isequal(b, [[3, 3, 3]]))

if __name__ == '__main__':
    unittest.main()
