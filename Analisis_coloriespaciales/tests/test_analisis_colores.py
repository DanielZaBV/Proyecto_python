import unittest
from Analisis_coloriespaciales.scripts.analisis_color import merge_similar_colors, round_color_value
from Analisis_coloriespaciales.scripts.generador_de_imagen import generate_image
from pathlib import Path

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

class TestGenerateImage(unittest.TestCase):
    def test_generate_sample_image(self):
        # Comprueba si la imagen se genera correctamente
        generate_image("test_image.png", width=100, height=100)
        # Verifica si la imagen existe
        self.assertTrue(Path("test_image.png").is_file())


if __name__ == '__main__':
    unittest.main()
