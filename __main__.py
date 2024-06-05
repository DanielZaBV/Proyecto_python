# __main__.py
from Analisis_coloriespaciales.procesador_de_imagen import cargar_y_dividir_imagen, procesar_bloque
from Analisis_coloriespaciales.utils import guardar_resultados
from Analisis_coloriespaciales.analisis_color import desnormalizar_valores, agrupar_y_normalizar_colores
import dask
import numpy as np
from PIL import Image

def main():
    # Solicitar al usuario el nombre de la imagen
    nombre_imagen = input("Ingrese el nombre de la imagen a analizar: ")
    if not nombre_imagen:
        print("Error: No se ingresó un nombre de imagen.")
        return

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
            return
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
                return

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
    guardar_resultados(selected_color_positions)
    valores_normalizados = [float(valor) for valor in selected_color_positions]
    colores_rgb = desnormalizar_valores(valores_normalizados, width, height)
    colores_agrupados = agrupar_y_normalizar_colores(colores_rgb, umbral)

if __name__ == "__main__":
    main()
