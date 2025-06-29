"""
filters.py

Parte 3: Filtragem e Picos
"""

import numpy as np
from typing import Tuple

def replace_negatives(v: np.ndarray, new_value: float) -> np.ndarray:
    """
    Substitui os valores negativos em um vetor por um novo valor.
    """
    v_copy = v.copy()
    v_copy[v_copy < 0] = new_value
    return v_copy

def local_peaks(series: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Identifica máximos locais em uma série temporal.
    """
    indices = []
    peaks = []
    for t in range(1, len(series) - 1):
        if series[t-1] < series[t] > series[t+1]:
            indices.append(t)
            peaks.append(series[t])
    return np.array(indices), np.array(peaks)
