from typing import List

from Analisis_coloriespaciales.scripts.analisis_color import  read_selected_colors, group_similar_colors, analyze_color_frequency

def analyze_colors(filename, width, height):
    values = read_selected_colors(filename)
    grouped_colors = group_similar_colors(values, width, height)
    color_frequency = analyze_color_frequency(grouped_colors, width, height)

    for cluster, colors in color_frequency.items():
        print(f"Cluster {cluster}:")
        for color, frequency in colors.items():
            print(f"  Color {color}: {frequency} veces")
