from typing import Dict
import numpy as np
import threading


def calcular_medias_moveis(acoes: Dict[str, np.ndarray], janela: int) -> Dict[str, np.ndarray]:
    """
    Calcula as médias móveis para várias ações em paralelo.

    Cada ação é processada por uma thread que calcula a média móvel com a janela especificada.

    Args:
        acoes (Dict[str, np.ndarray]): Dicionário onde as chaves são nomes das ações e os valores são arrays de preços.
        janela (int): Tamanho da janela para o cálculo da média móvel.

    Returns:
        Dict[str, np.ndarray]: Dicionário com as médias móveis de cada ação.
    """
    resultado: Dict[str, np.ndarray] = {}
    lock = threading.Lock()

    def calcular(acao: str, precos: np.ndarray) -> None:
        medias = np.convolve(precos, np.ones(janela)/janela, mode='valid')
        with lock:
            resultado[acao] = medias

    threads = [threading.Thread(target=calcular, args=(acao, precos))
               for acao, precos in acoes.items()]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return resultado


def calcular_volatilidade(retornos: np.ndarray, janela: int, num_threads: int) -> np.ndarray:
    """
    Calcula a volatilidade (desvio padrão) em janelas móveis sobre um array de retornos, utilizando múltiplas threads.

    O array é particionado entre as threads, respeitando a sobreposição das janelas.

    Args:
        retornos (np.ndarray): Array de retornos diários.
        janela (int): Tamanho da janela para o cálculo da volatilidade.
        num_threads (int): Número de threads a serem usadas.

    Returns:
        np.ndarray: Array com as volatilidades calculadas para cada janela.
    """
    n = len(retornos)
    resultado = [None] * (n - janela + 1)
    lock = threading.Lock()

    def worker(inicio: int, fim: int) -> None:
        for i in range(inicio, min(fim, n - janela + 1)):
            janela_dados = retornos[i:i+janela]
            vol = np.std(janela_dados)
            with lock:
                resultado[i] = vol

    # Divide os índices de forma balanceada
    blocos = np.linspace(0, n - janela + 1, num_threads + 1, dtype=int)
    threads = [
        threading.Thread(target=worker, args=(blocos[i], blocos[i+1]))
        for i in range(num_threads)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return np.array(resultado, dtype=np.float64)
