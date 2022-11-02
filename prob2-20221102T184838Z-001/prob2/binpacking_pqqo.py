#!/usr/bin/env python3
import sys
from typing import List, TextIO


def process(C: int, w: list[int]) -> list[int]:
    contenedores: list[int] = [0] * len(w)
    free: list[int] = []

    #indices ordenados
    indices = sorted(range(len(w)), key = lambda i: -w[i])

    for i in indices:
        obj = w[i]
        #Elegir contenedor
        nc = None
        for c in range(len(free)):
            if free[c] >= obj:
                nc = c
                break
        if nc == None:
            free.append(C)
            nc = len(free) - 1

        #insertar en contenedor
        free[nc] -= obj
        contenedores[i] = nc

    return contenedores

def read_data(f: TextIO) -> tuple[int,list[int]]:
    C = int(f.readline())
    w = [int(linea) for linea in f.readlines()]
    return C,w


def show_results(contenedores: list[int]):
    for c in contenedores:
        print(c)


if __name__ == "__main__":
    C, w = read_data(sys.stdin)
    contenedores = process(C,w)
    show_results(contenedores)
