"""
operations.py

Parte 2: Operações em Vetores e Matrizes
"""

import numpy as np

def rotate_90(A: np.ndarray) -> np.ndarray:
    """
    Rotaciona uma matriz quadrada 90° no sentido horário.
    """
    B = A.T
    return np.array([row[::-1] for row in B])

def sum_subdiagonals(A: np.ndarray, k: int) -> float:
    """
    Soma os elementos da k-ésima subdiagonal.
    """
    n = A.shape[0]
    return sum(A[i, i - k] for i in range(k, n))

def block_matmul(A: np.ndarray, B: np.ndarray, block_size: int) -> np.ndarray:
    """
    Multiplicação de matrizes por blocos.
    """
    m, p = A.shape
    _, n = B.shape
    C = np.zeros((m, n))
    for i0 in range(0, m, block_size):
        for j0 in range(0, n, block_size):
            for k0 in range(0, p, block_size):
                A_block = A[i0:i0+block_size, k0:k0+block_size]
                B_block = B[k0:k0+block_size, j0:j0+block_size]
                C[i0:i0+block_size, j0:j0+block_size] += A_block @ B_block
    return C
