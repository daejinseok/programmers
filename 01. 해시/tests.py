import unittest
import tel_list

class Test(unittest.TestCase):

    def test_add(self):
        c = tel_list.add(20, 30)
        self.assertEqual(c, 50)

if __name__ == '__main__':
    unittest.main()




