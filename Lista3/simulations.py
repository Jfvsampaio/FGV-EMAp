"""
simulations.py

Parte 1: Simulação de Preços e Análise de Retornos
"""

import numpy as np

def simular_precos(S0: float, sigma: float, days: int) -> np.ndarray:
    """
    Gera uma série temporal de preços com ruído gaussiano.
    """
    precos = [S0]
    for _ in range(days):
        preco = precos[-1] + np.random.normal(0, sigma)
        precos.append(preco)
    return np.array(precos)

def calc_retornos_simples(prices: np.ndarray) -> np.ndarray:
    """
    Calcula os retornos simples dados os preços.
    """
    return (prices[1:] - prices[:-1]) / prices[:-1]

def calc_retornos_log(prices: np.ndarray) -> np.ndarray:
    """
    Calcula os log-retornos dados os preços.
    """
    return np.log(prices[1:] / prices[:-1])

def sma(returns: np.ndarray, window: int) -> np.ndarray:
    """
    Calcula a média móvel simples (SMA).
    """
    return np.array([np.mean(returns[i-window+1:i+1]) for i in range(window-1, len(returns))])

def rolling_std(returns: np.ndarray, window: int, days_size: int = 0) -> np.ndarray:
    """
    Calcula o desvio padrão móvel com normalização ajustável.
    """
    stds = []
    for i in range(window - 1, len(returns)):
        window_data = returns[i - window + 1:i + 1]
        mean = np.mean(window_data)
        std = np.sqrt(np.sum((window_data - mean)**2) / (window - days_size))
        stds.append(std)
    return np.array(stds)
