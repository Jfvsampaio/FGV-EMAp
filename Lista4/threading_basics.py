from typing import List, Dict, Any
import threading
import random
import time

def simular_traders(num_traders: int, num_ordens: int) -> Dict[str, List[Dict[str, Any]]]:
    """
    Simula múltiplos traders inserindo ordens de compra e venda concorrentemente.

    Cada trader é representado por uma thread que insere ordens em um livro de ordens (order book)
    compartilhado. A sincronização é garantida por um threading.Lock para evitar condições de corrida.

    Args:
        num_traders (int): Número de traders (threads).
        num_ordens (int): Número de ordens que cada trader irá colocar.

    Returns:
        Dict[str, List[Dict[str, Any]]]: Estado final do livro de ordens, contendo listas de ordens de compra e venda.
    """
    order_book = {'buy': [], 'sell': []}
    lock = threading.Lock()
    ordem_id = 0

    def trader() -> None:
        nonlocal ordem_id
        for _ in range(num_ordens):
            with lock:
                ordem = {
                    'id': ordem_id,
                    'price': round(random.uniform(10, 100), 2),
                    'quantity': random.randint(1, 100)
                }
                ordem_id += 1
                lado = random.choice(['buy', 'sell'])
                order_book[lado].append(ordem)

    threads = [threading.Thread(target=trader) for _ in range(num_traders)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return order_book


def simular_feeds_de_dados(acoes: List[str], tempo_total: int) -> Dict[str, float]:
    """
    Simula múltiplos feeds de dados atualizando preços de ações concorrentemente.

    Cada ação tem sua própria thread que atualiza seu preço a cada 1–3 segundos.
    Outra thread imprime os preços a cada 5 segundos.
    Um Lock garante acesso seguro ao dicionário de preços compartilhado.

    Args:
        acoes (List[str]): Lista com os nomes das ações (ex: ['AAPL', 'GOOG']).
        tempo_total (int): Duração total da simulação (em segundos).

    Returns:
        Dict[str, float]: Dicionário final com os preços atualizados das ações.
    """
    prices: Dict[str, float] = {acao: random.uniform(50, 150) for acao in acoes}
    lock = threading.Lock()
    running = True

    def feed(acao: str) -> None:
        nonlocal running
        while running:
            time.sleep(random.uniform(1, 3))
            with lock:
                prices[acao] += random.uniform(-5, 5)

    def imprimir_precos() -> None:
        nonlocal running
        while running:
            time.sleep(5)
            with lock:
                print({k: round(v, 2) for k, v in prices.items()})

    threads = [threading.Thread(target=feed, args=(acao,)) for acao in acoes]
    threads.append(threading.Thread(target=imprimir_precos))

    for t in threads:
        t.start()
    time.sleep(tempo_total)
    running = False
    for t in threads:
        t.join()

    return {k: round(v, 2) for k, v in prices.items()}
