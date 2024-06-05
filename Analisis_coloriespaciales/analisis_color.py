import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def desnormalizar_valores(valores_normalizados, width, height):
    colores_rgb = []
    for valor in valores_normalizados:
        combined_value = float(valor)
        
        # Suponiendo que los valores combinados se distribuyen uniformemente:
        norm_x = combined_value * width
        norm_y = combined_value * height
        norm_r = combined_value * 255
        norm_g = combined_value * 255
        norm_b = combined_value * 255
        
        # Desnormalizamos los valores
        x = int(norm_x * width)
        y = int(norm_y * height)
        r = int(norm_r * 255)
        g = int(norm_g * 255)
        b = int(norm_b * 255)
        
        colores_rgb.append((r, g, b))
    return colores_rgb

def agrupar_y_normalizar_colores(colores_rgb, umbral=20):
    def distancia_rgb(color1, color2):
        return sum(abs(c1 - c2) for c1, c2 in zip(color1, color2))
    
    grupos = []
    colores_normalizados = []

    for color in colores_rgb:
        agregado = False
        for grupo in grupos:
            if all(abs(color[i] - grupo[0][i]) <= umbral for i in range(3)):
                grupo.append(color)
                agregado = True
                break
        if not agregado:
            grupos.append([color])
    
    for grupo in grupos:
        r_promedio = int(sum(c[0] for c in grupo) / len(grupo))
        g_promedio = int(sum(c[1] for c in grupo) / len(grupo))
        b_promedio = int(sum(c[2] for c in grupo) / len(grupo))
        colores_normalizados.append((r_promedio, g_promedio, b_promedio))
    
    return colores_normalizados

def agrupar_colores_por_clusters(colores_normalizados, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(colores_normalizados)
    return clusters, kmeans.cluster_centers_

def analizar_distribucion_colores(clusters, colores_normalizados):
    unique, counts = np.unique(clusters, return_counts=True)
    color_distribution = dict(zip(unique, counts))
    
    for cluster in color_distribution.keys():
        indices = np.where(clusters == cluster)
        colores_en_cluster = colores_normalizados[indices]
        print(f"Cluster {cluster}:")
        print(f"  Cantidad de Colores: {color_distribution[cluster]}")
        print(f"  Colores: {colores_en_cluster}")

    return color_distribution

def visualizar_clusters(image_shape, clusters):
    clustered_image = clusters.reshape(image_shape[:2])
    plt.figure(figsize=(10, 10))
    plt.imshow(clustered_image, cmap='viridis')
    plt.title('Segmentación de la Imagen en Clusters de Colores')
    plt.axis('off')
    plt.show()

def plot_color_distribution(color_distribution):
    plt.bar(color_distribution.keys(), color_distribution.values())
    plt.xlabel('Cluster')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de Colores en Cada Cluster')
    plt.show()