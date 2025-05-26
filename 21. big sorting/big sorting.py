#!/bin/python3

import sys

def bigSorting(unsorted):
    sorted_list = sorted(unsorted, key=lambda x: (len(x), x))
    return sorted_list

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    unsorted = data[1:n+1]
    
    result = bigSorting(unsorted)
    
    # Imprimir resultados
    print("\n".join(result))
