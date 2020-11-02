import unittest
import pandas as pd
from main import productionYear
from main import yearing
movies = pd.read_csv('movies.csv', index_col = 'movieId')

class TestMain(unittest.TestCase):
    def test_productionYear(self):
        test_string = "Дзідзьо контрабас 2 (2016)"
        result = productionYear(test_string)
        self.assertEqual(result, 2016)

    def test_productionYear2(self):
        test_string = "Дзідзьо контрабас (1992) (2018)"
        result = productionYear(test_string)
        self.assertEqual(result, 2018)

    def test_productionYear3(self):
        test_string = ""
        result = productionYear(test_string)
        self.assertEqual(result, 1950)

    def test_yearing(self):
        test_int = -1
        result = yearing(test_int)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()