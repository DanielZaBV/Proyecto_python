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
