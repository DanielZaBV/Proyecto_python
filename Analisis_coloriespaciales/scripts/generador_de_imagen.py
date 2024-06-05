from PIL import Image
import numpy as np

def generate_image(width, height, filename):
    """
    Genera una imagen RGB de 8 bits con píxeles aleatorios y la guarda en un archivo.

    Parameters:
    - width (int): Ancho de la imagen en píxeles.
    - height (int): Alto de la imagen en píxeles.
    - filename (str): Nombre del archivo donde se guardará la imagen generada.

    Returns:
    - None
    """
    # Crear una imagen RGB de 8 bits
    image = Image.new('RGB', (width, height))

    # Generar píxeles aleatorios
    pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(pixels)

    # Guardar la imagen
    image.save(filename)
