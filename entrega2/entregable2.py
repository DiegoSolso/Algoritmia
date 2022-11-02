#!/usr/bin/env python3
import sys
from typing import TextIO

# Folleto en inglés es Leaflet
Leaflet = tuple[int, int, int]          # (num_folleto, anchura, altura)
LeafletPos = tuple[int, int, int, int]  # (num_folleto, num_hoja_de_imprenta, pos_x ,pos_y)


# Lee la instancia por la entrada estándar (ver apartado 1.1)
# Devuelve el tamaño del papel de la imprenta y la lista de folletos
def read_data(f: TextIO) -> tuple[int, list[Leaflet]]:
    M = f.readline()
    l = [Leaflet]
    for linea in f:
        l.append(linea)
    return tuple(M,l)


# Recibe el tamaño del papel de la imprenta y la lista de folletos
# Devuelve tamaño del papel y lista de folletos
def process(paper_size: int, leaflet_list: list[Leaflet]) -> list[LeafletPos]:
    indices = sorted(range(len(leaflet_list)), key=lambda i: -leaflet_list[i][2])
    ocupados=[paper_size**2]
    for x in paper_size**2:
        ocupados[x] = False
    cuadrados_creados=1
    for i in indices:
        if llenar(ocupados,leaflet_list[i]) is not True:
# Nuevo Cuadrado



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
