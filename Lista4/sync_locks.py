from typing import List, Tuple, Dict
import threading
import time
import random


def gerenciar_risco(total_risco: float, estrategias: List[Tuple[str, float]], tempo_total: int) -> Dict[str, float]:
    """
    Simula a alocação concorrente de risco entre várias estratégias, com sincronização via Lock.

    Cada estratégia roda em uma thread separada e tenta alocar parte do risco total disponível.
    Se não houver risco suficiente, a thread espera. A alocação é protegida por um Lock.

    Args:
        total_risco (float): Valor total de risco disponível para alocação.
        estrategias (List[Tuple[str, float]]): Lista de tuplas (nome da estratégia, risco desejado).
        tempo_total (int): Duração da simulação em segundos.

    Returns:
        Dict[str, float]: Risco alocado para cada estratégia ao final da simulação.
    """
    risco_restante = total_risco
    risco_alocado: Dict[str, float] = {}
    lock = threading.Lock()
    start_time = time.time()

    def alocar_estrategia(nome: str, risco_desejado: float) -> None:
        nonlocal risco_restante
        while time.time() - start_time < tempo_total:
            with lock:
                if risco_restante >= risco_desejado:
                    risco_restante -= risco_desejado
                    risco_alocado[nome] = risco_desejado
                    return
            time.sleep(0.1)

    threads = [
        threading.Thread(target=alocar_estrategia, args=(nome, risco))
        for nome, risco in estrategias
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return risco_alocado


def monitorar_acoes(acoes: List[str], valor_alvo: float) -> List[str]:
    """
    Simula o monitoramento concorrente de ações para detectar se o valor-alvo foi atingido.

    Cada ação é monitorada por uma thread, que gera um preço anterior e um atual com atraso aleatório.
    Se o valor-alvo estiver entre os dois valores, a ação é registrada como 'atingida'.

    Args:
        acoes (List[str]): Lista com os nomes das ações a monitorar.
        valor_alvo (float): Valor a ser monitorado entre o preço anterior e o atual.

    Returns:
        List[str]: Lista com os nomes das ações cujo preço atingiu ou ultrapassou o valor-alvo.
    """
    atingidas: List[str] = []
    lock = threading.Lock()

    def monitorar(acao: str) -> None:
        time.sleep(random.uniform(0.1, 0.5))
        preco_anterior = random.uniform(80, 120)
        time.sleep(random.uniform(0.1, 0.5))
        preco_atual = random.uniform(80, 120)

        minimo = min(preco_anterior, preco_atual)
        maximo = max(preco_anterior, preco_atual)

        if minimo <= valor_alvo <= maximo:
            with lock:
                atingidas.append(acao)

    threads = [threading.Thread(target=monitorar, args=(acao,)) for acao in acoes]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return atingidas
