
def guardar_resultados(selected_color_positions, file_path="..\data\selected_colors.txt"):
    with open(file_path, "w") as f:
        f.write(":".join(selected_color_positions))
    print(f"La selección de colores se ha guardado en '{file_path}'")

def cargar_resultados(filename):
    with open(filename, 'r') as f:
        resultados = f.read().split("\n")
    return resultados