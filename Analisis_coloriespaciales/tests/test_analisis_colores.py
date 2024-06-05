# tests/test_analyze.py

import unittest
from Analisis_coloriespaciales.scripts.analisis_color import merge_similar_colors, round_color_value

class TestAnalyze(unittest.TestCase):
    def test_merge_similar_colors(self):
        colors = [(20, 20, 20), (22, 22, 22), (25, 25, 25), (30, 30, 30)]
        merged = merge_similar_colors(colors, threshold=5)
        expected = {(20, 20, 20): 2, (25, 25, 25): 1, (30, 30, 30): 1}
        self.assertEqual(merged, expected)


class TestUtils(unittest.TestCase):
    def test_round_color_value(self):
        rounded = round_color_value(28, round_to=10)
        self.assertEqual(rounded, 30)



if __name__ == '__main__':
    unittest.main()
