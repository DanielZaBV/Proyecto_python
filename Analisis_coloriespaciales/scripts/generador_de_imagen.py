from PIL import Image
import numpy as np

def generate_image(width, height, filename):
    # Crear una imagen RGB de 8 bits
    image = Image.new('RGB', (width, height))

    # Generar píxeles aleatorios
    pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(pixels)

    # Guardar la imagen
    image.save(filename)
