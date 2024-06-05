import numpy as np
import dask
from PIL import Image
from Analisis_coloriespaciales.procesador_de_imagen import cargar_y_dividir_imagen, procesar_bloque
from Analisis_coloriespaciales.utils import guardar_resultados, cargar_resultados
from Analisis_coloriespaciales.analisis_color import desnormalizar_valores, agrupar_colores_por_clusters, analizar_distribucion_colores, visualizar_clusters, plot_color_distribution

def main():
    nombre_imagen = input("Ingrese el nombre de la imagen a analizar: ")
    if not nombre_imagen:
        print("Error: No se ingresó un nombre de imagen.")
        return

    block_size = 317
    umbral = 20
    image = Image.open(nombre_imagen)
    width, height = image.size
    image_array = cargar_y_dividir_imagen(nombre_imagen, block_size)

    # Suponiendo que el procesamiento de la imagen y la obtención de selected_color_positions ya se ha realizado
    selected_color_positions = cargar_resultados('selected_colors.txt')

    # Desnormalizar los valores para recuperar los colores RGB
    valores_normalizados = [float(valor) for valor in selected_color_positions]
    colores_rgb = desnormalizar_valores(valores_normalizados, width, height)

    # Agrupar los colores utilizando K-means
    n_clusters = 5  # Ajustar según sea necesario
    clusters, cluster_centers = agrupar_colores_por_clusters(colores_rgb, n_clusters)

    # Analizar la distribución de colores en cada cluster
    color_distribution = analizar_distribucion_colores(clusters, colores_rgb)

    # Visualizar los clusters en la imagen
    visualizar_clusters(image_array.shape, clusters)

    # Mostrar la distribución de colores en un gráfico de barras
    plot_color_distribution(color_distribution)

if __name__ == "__main__":
    main()
