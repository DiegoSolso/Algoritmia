#!/usr/bin/env python3.9
import sys
from random import shuffle, seed
from typing import TextIO, Optional

from algoritmia.datastructures.graphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo

Vertex = tuple[int, int]
Edge = tuple[Vertex, Vertex]

NO_VALID_WALL = 'NO VALID WALL'

# Función ya implementada
# Esta función utiliza un MFSet para crear un laberinto, pero le añade n aristas
# adicionales que provocan que el laberinto tenga ciclos.
def create_labyrinth(rows: int, cols: int, n: int, s: int) -> UndirectedGraph[Vertex]:
    vertices: list[Vertex] = [(r, c) for r in range(rows) for c in range(cols)]
    mfs: MergeFindSet[Vertex] = MergeFindSet((v,) for v in vertices)
    edges: list[Edge] = [((r, c), (r + 1, c)) for r in range(rows - 1) for c in range(cols)]
    edges.extend([((r, c), (r, c + 1)) for r in range(rows) for c in range(cols - 1)])
    seed(s)
    shuffle(edges)
    corridors: list[Edge] = []
    for (u, v) in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        elif n > 0:
            n -= 1
            corridors.append((u, v))
    return UndirectedGraph(E=corridors)



def process(lab: UndirectedGraph[Vertex], rows: int, cols: int) -> tuple[Optional[Edge], int, int]:
    initial_map = map_maker(lab, (0,0))
    ending_map = map_maker(lab, (rows-1, cols-1))
    lenght_before = initial_map.get((rows-1, cols-1))
    length_after = lenght_before
    street = None
    for r in range(rows):
        for c in range(cols):
                actuall_cell = (r, c)
                row_below = (r + 1, c)
                right_col = (r, c + 1)
                cell = initial_map.get(actuall_cell)
                under_cell = ending_map.get(row_below)
                right_cell = ending_map.get(right_col)
                if cell is not None:
                    if under_cell is not None:
                        street,length_after = check_wall(cell, initial_map, ending_map, street, length_after, row_below, actuall_cell, under_cell)

                    if right_cell is not None:
                        street,length_after = check_wall(cell, initial_map, ending_map, street, length_after, right_col, actuall_cell, right_cell)
               

    return street, lenght_before, length_after


def map_maker(g: UndirectedGraph[Vertex], source: Vertex):
    map = {}
    map[source] = 0
    pending = Fifo()
    seen = set()
    seen.add(source)
    pending.push((source, source))
    while len(pending) > 0:
        u, v = pending.pop()
        for suc in g.succs(v):
            if suc not in seen:
                map[suc] = map[v] + 1
                pending.push((v, suc))
                seen.add(suc)
    return map


def check_wall(cell: int,initial_map: dict[tuple[int, int], int],ending_map: dict[tuple[int, int], int],street,length_after,next: (int,int),actual_cell: (int,int),next_cell: int):
    ret=street
    minimo = min(cell + next_cell + 1, initial_map.get(next) + ending_map.get(actual_cell) + 1)
    if minimo == length_after and street is not None:
        if street > (actual_cell, next):
            ret = (actual_cell, next)
    elif minimo < length_after:
        length_after = minimo
        ret = (actual_cell, next)
    return ret,length_after


def read_data(f: TextIO) -> tuple[UndirectedGraph[Vertex], int, int]:
    rows = int(f.readline())
    cols = int(f.readline())
    n= int(f.readline())
    s= int(f.readline())
    g = create_labyrinth(rows, cols, n, s)
    return g,rows, cols


def show_results(edge_to_add: Optional[Edge], length_before: int, length_after: int):
    if edge_to_add is None:
        print(NO_VALID_WALL)
    else:
        added1 = edge_to_add[0]
        added2 = edge_to_add[1]
        print(f"{added1[0]} {added1[1]} {added2[0]} {added2[1]}")

    print(length_before)
    print(length_after)

if __name__ == '__main__':
    graph0, rows0, cols0 = read_data(sys.stdin)
    edge_to_add0, length_before0, length_after0 = process(graph0, rows0, cols0)
    show_results(edge_to_add0, length_before0, length_after0)