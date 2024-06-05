# Analisis_coloriespaciales/__main__.py

from Analisis_coloriespaciales.utils.utils import analyze_colors

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Uso: python -m Analisis_coloriespaciales <archivo_selected_colors.txt> <ancho_imagen> <alto_imagen>")
        sys.exit(1)

    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    analyze_colors(filename, width, height)
