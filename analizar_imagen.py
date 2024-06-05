import dask.array as da
import dask
from dask import delayed
import numpy as np
from PIL import Image

# Ajustar el límite de tamaño de imagen permitido por PIL/Pillow
Image.MAX_IMAGE_PIXELS = None

# Función para cargar y dividir la imagen en bloques usando Dask
def cargar_y_dividir_imagen(nombre_imagen, block_size):
    image = Image.open(nombre_imagen)
    image_array = np.array(image)
    dask_array = da.from_array(image_array, chunks=(block_size, block_size, 3))
    return dask_array

# Función para procesar cada bloque
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
                    combined_value = (norm_x + norm_y + norm_r + norm_g + norm_b) / 5  # Promedio de los valores normalizados
                    block_data.append(f"{combined_value:.6f}")
    return block_data

# Solicitar al usuario el nombre de la imagen
nombre_imagen = input("Ingrese el nombre de la imagen a analizar: ")
if not nombre_imagen:
    print("Error: No se ingresó un nombre de imagen.")
    exit()

# Solicitar al usuario si desea buscar uno o varios colores
while True:
    num_colores = input("¿Desea buscar uno o varios colores? (Ingrese 'uno' o 'varios'): ").lower()
    if num_colores == 'uno' or num_colores == 'varios':
        break
    else:
        print("Opción no válida. Por favor, ingrese 'uno' o 'varios'.")

# Solicitar al usuario el color o colores RGB
selected_colors = []
if num_colores == 'uno':
    try:
        r = int(input("Ingrese el valor R del color (0-255): "))
        g = int(input("Ingrese el valor G del color (0-255): "))
        b = int(input("Ingrese el valor B del color (0-255): "))
        selected_colors.append((r, g, b))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para R, G y B.")
        exit()
else:
    while True:
        try:
            r = int(input("Ingrese el valor R del color (0-255): "))
            g = int(input("Ingrese el valor G del color (0-255): "))
            b = int(input("Ingrese el valor B del color (0-255): "))
            selected_colors.append((r, g, b))
            agregar_otro = input("¿Desea agregar otro color? (Ingrese 'si' o 'no'): ").lower()
            if agregar_otro != 'si':
                break
        except ValueError:
            print("Error: Ingrese valores numéricos válidos para R, G y B.")
            exit()

# Cargar la imagen y dividir en bloques
block_size = 317
umbral = 20
image = Image.open(nombre_imagen)
width, height = image.size
image_array = cargar_y_dividir_imagen(nombre_imagen, block_size)

# Procesar bloques
delayed_results = []
for block_index in np.ndindex(image_array.numblocks[:2]):
    block = image_array.blocks[block_index].compute()
    result = procesar_bloque(block, block_index, selected_colors, block_size, width, height, umbral)
    delayed_results.append(result)

selected_color_positions = dask.compute(*delayed_results)
selected_color_positions = [item for sublist in selected_color_positions for item in sublist]

# Guardar resultados
with open("selected_colors.txt", "w") as f:
    f.write(":".join(selected_color_positions))

print("La selección de colores se ha guardado en 'selected_colors.txt'")