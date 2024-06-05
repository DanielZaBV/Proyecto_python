# image_processing.py
import dask.array as da
from dask import delayed
import numpy as np
from PIL import Image

# Ajustar el límite de tamaño de imagen permitido por PIL/Pillow
Image.MAX_IMAGE_PIXELS = None

def cargar_y_dividir_imagen(nombre_imagen, block_size):
    image = Image.open(nombre_imagen)
    image_array = np.array(image)
    dask_array = da.from_array(image_array, chunks=(block_size, block_size, 3))
    return dask_array

@delayed
def procesar_bloque(block, block_index, selected_colors, block_size, width, height, umbral):
    y, x = block_index
    block_data = []
    for j in range(block.shape[0]):
        for i in range(block.shape[1]):
            pixel = tuple(block[j, i])
            for selected_color in selected_colors:
                if all(abs(pixel[k] - selected_color[k]) <= umbral for k in range(3)):
                    norm_x = (x + i) / width
                    norm_y = (y + j) / height
                    norm_r = pixel[0] / 255
                    norm_g = pixel[1] / 255
                    norm_b = pixel[2] / 255
                    combined_value = (norm_x + norm_y + norm_r + norm_g + norm_b) / 5
                    block_data.append(f"{combined_value:.6f}")
    return block_data
