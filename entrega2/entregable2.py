#!/usr/bin/env python3
import sys
from typing import TextIO

# Folleto en inglés es Leaflet
Leaflet = tuple[int, int, int]          # (num_folleto, anchura, altura)
LeafletPos = tuple[int, int, int, int]  # (num_folleto, num_hoja_de_imprenta, pos_x ,pos_y)


# Lee la instancia por la entrada estándar (ver apartado 1.1)
# Devuelve el tamaño del papel de la imprenta y la lista de folletos
def read_data(f: TextIO) -> tuple[int, list[Leaflet]]:
    M = int(f.readline())
    l = []
    for linea in f:
        num, width, height = linea.split(" ")
        l.append((int(num), int(width), int(height)))
    return M, l


# Recibe el tamaño del papel de la imprenta y la lista de folletos
# Devuelve tamaño del papel y lista de folletos
def process(paper_size: int, leaflet_list: list[Leaflet]) -> list[LeafletPos]:
    leaflet_list.sort(key=lambda element: (element[1], element[2]), reverse=True)
    cuadrados_creados = 1
    ocupado_x = list([0, 0])
    ocupado_y = list([0, 0])
    base_anterior = 0
    crearCuadrado = True
    cuadrados = []
    aux = [ocupado_x, ocupado_y, base_anterior]
    cuadrados.append(aux)
    resultado = []
    i = 0
    h = 0
    stp = len(leaflet_list)//1000
    if stp == 0:
        stp = 1
    while i < len(leaflet_list):
        h += 1
        for j in range(h % stp, cuadrados_creados, stp):
            tupla = llenar(paper_size, cuadrados[j][0], cuadrados[j][1], cuadrados[j][2], leaflet_list[i])
            crearCuadrado = tupla[5]

            if crearCuadrado is False:
                cuadrados[j][0] = tupla[0]
                cuadrados[j][1] = tupla[1]
                cuadrados[j][2] = tupla[4]
                t = leaflet_list[i][0], j + 1, tupla[2], tupla[3]
                resultado.append(t)
                break

        if crearCuadrado is True:
            cuadrados_creados += 1
            ocupado_x = list([0, 0])
            ocupado_y = list([0, 0])
            base_anterior = 0
            aux = [ocupado_x, ocupado_y, base_anterior]
            cuadrados.append(aux)
            tupla = llenar(paper_size, cuadrados[len(cuadrados) - 1][0], cuadrados[len(cuadrados) - 1][1],
                           cuadrados[len(cuadrados) - 1][2], leaflet_list[i])
            cuadrados[len(cuadrados) - 1][0] = tupla[0]
            cuadrados[len(cuadrados) - 1][1] = tupla[1]
            cuadrados[len(cuadrados) - 1][2] = tupla[4]
            t = leaflet_list[i][0], cuadrados_creados, tupla[2], tupla[3]
            resultado.append(t)

        i += 1

    return resultado


def llenar(ocupados:list[bool],leaflet: Leaflet)-> list[tuple[int,int,bool]]:

    return True

# Muestra por la salida estandar las posiciones de los folletos (ver apartado 1.2)
def show_results(leafletpos_list: list[LeafletPos]):
    for l in leafletpos_list:
        s = l[0]+" "+l[1]+" "+l[2]+" "+l[3]
        print(s)


if __name__ == '__main__':
    paper_size0, leaflet_list0 = read_data(sys.stdin)
    leafletpos_list0 = process(paper_size0, leaflet_list0)
    show_results(leafletpos_list0)
