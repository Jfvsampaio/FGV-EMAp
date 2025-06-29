# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 19:20:06 2025

@author: jsampaio
"""
import math
import itertools
import random
import urllib.request
import os
import csv
import sys


# Parte 1
# Função 1 - Valor Futuro com Juros Compostos
def future_value(pv, r, n, t):
    """
    Calcula o valor futuro com capitalização composta.
    FV = PV * (1 + r/n)^(n*t)
    """
    if not all(isinstance(x, (int, float)) for x in [pv, r, n, t]):
        raise ValueError("Todos os parâmetros devem ser números.")
    if n <= 0:
        raise ValueError("O número de períodos por ano deve ser positivo.")

    fator = 1 + r / n
    expoente = n * t
    return pv * math.pow(fator, expoente)


# Função 2 - Desvio Padrão de uma Lista de Retornos
def standard_deviation(returns):
    """
    Calcula o desvio padrão populacional de uma lista de números.
    stdev = sqrt(1/n * (sum(x - media)) ^ 2)
    """
    if not isinstance(returns, list) or not all(isinstance(x, (int, float)) for x in returns):
        raise ValueError("A entrada deve ser uma lista de números.")
    if len(returns) == 0:
        raise ValueError("A lista não pode estar vazia.")

    media = sum(returns) / len(returns)
    variancia = sum((x - media) ** 2 for x in returns) / len(returns)
    return math.sqrt(variancia)


# Função 3 - Tempo para Dobrar o Capital com Capitalização Contínua
def time_to_double(r):
    """
    Calcula o tempo necessário para dobrar o capital com juros contínuos.
    t = ln(2) / ln(1 + r)
    """
    if not isinstance(r, (int, float)):
        raise ValueError("A taxa deve ser um número.")
    if r <= 0:
        raise ValueError("A taxa de juros deve ser positiva.")

    return math.log(2) / math.log(1 + r)


# Testes automatizados
if __name__ == "__main__":
    # Teste função future_value
    fv = future_value(100000, 0.1275, 12, 10)
    print(f"Valor Futuro: R$ {fv:.2f}")

    # Teste função standard_deviation
    dados = [0.02, 0.03, 0.01, -0.01, 0.00]
    dp = standard_deviation(dados)
    print(f"Desvio Padrão: {dp:.4f}")

    # Teste função time_to_double
    tempo = time_to_double(0.1275)
    print(f"Tempo para dobrar: {tempo:.2f} anos")




# Parte 2

# Função 1 - Combinações de ativos
def portfolio_combinations(assets, k):
    """
    Retorna todas as combinações possíveis de k ativos a partir de uma lista.
    
    Parâmetros:
    - assets: lista de nomes de ativos (strings)
    - k: tamanho da combinação

    Retorna:
    - Lista de tuplas com combinações de ativos
    """
    if not isinstance(assets, list) or not all(isinstance(a, str) for a in assets):
        raise ValueError("Assets deve ser uma lista de strings.")
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k deve ser um inteiro positivo.")
    if k > len(assets):
        raise ValueError("k não pode ser maior que o número de ativos.")

    return list(itertools.combinations(assets, k))


# Função 2 - Média Móvel usando itertools
def moving_average(prices, window):
    """
    Calcula a média móvel de uma lista de preços usando janelas deslizantes.

    Parâmetros:
    - prices: lista de floats
    - window: tamanho da janela (int)

    Retorna:
    - Lista de médias móveis (float)
    """
    if not isinstance(prices, list) or not all(isinstance(p, (int, float)) for p in prices):
        raise ValueError("prices deve ser uma lista de números.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window deve ser um inteiro positivo.")
    if window > len(prices):
        raise ValueError("A janela não pode ser maior que o tamanho da lista.")

    iteradores = itertools.tee(prices, window)
    for i, it in enumerate(iteradores):
        for _ in range(i):
            next(it, None)

    janelas = zip(*iteradores)
    return [sum(janela) / window for janela in janelas]


# Testes principais
if __name__ == "__main__":
    # Teste da função de combinação
    ativos = ["PETR4", "VALE3", "ITUB4", "B3SA3"]
    n_ativos = 2
    combinacoes = portfolio_combinations(ativos, n_ativos)
    print(f"Combinações de {n_ativos} ativos:", combinacoes)

    # Teste da média móvel
    precos = [10, 11, 12, 13, 14, 15]
    janelas = 3
    media_mov = moving_average(precos, janelas)
    print(f"Média móvel de {janelas} janelas):", media_mov)



# Parte 3

# Função - Simulação de Preços de Ações com Distribuição Normal
def simulate_stock_price(initial_price, mu, sigma, days):
    """
    Simula uma trajetória de preço de ação com base em movimentos diários aleatórios,
    com distribuição normal dos retornos.

    Parâmetros:
    - initial_price: preço inicial da ação (float)
    - mu: retorno médio esperado por dia (float)
    - sigma: volatilidade (desvio padrão) dos retornos diários (float)
    - days: número de dias a simular (int)

    Retorna:
    - Lista com os preços simulados
    """
    if not all(isinstance(x, (int, float)) for x in [initial_price, mu, sigma, days]):
        raise ValueError("Todos os parâmetros devem ser números.")
    if initial_price <= 0 or sigma < 0 or days <= 0:
        raise ValueError("Preço inicial deve ser > 0, sigma >= 0 e dias > 0.")

    prices = [initial_price]
    for _ in range(days):
        retorno_diario = random.gauss(mu, sigma)
        novo_preco = prices[-1] * (1 + retorno_diario)
        prices.append(novo_preco)

    return prices


# Teste principal
if __name__ == "__main__":
    preco_inicial = 100.0
    media = 0.00     # retorno médio
    volatilidade = 0.01  # desvio padrão
    dias = 10

    simulacao = simulate_stock_price(preco_inicial, media, volatilidade, dias)
    print("Preços simulados para 10 dias:")
    print(simulacao)


# Função - Download e Merge de CSVs do BLS
def download_and_merge(years_quarters, output_file):
    """
    Faz o download de arquivos CSV do Bureau of Labor Statistics (BLS) com base em ano e trimestre,
    salva localmente na pasta 'data/' e concatena em um único CSV de saída.

    Parâmetros:
    - years_quarters: lista de tuplas (ano, trimestre), por exemplo [(2024, 1), (2024, 2)]
    - output_file: caminho do arquivo CSV final mesclado

    Resultado:
    - Gera arquivo CSV com os dados concatenados em 'output_file'
    """
    if not isinstance(years_quarters, list) or not all(isinstance(yq, tuple) and len(yq) == 2 for yq in years_quarters):
        raise ValueError("years_quarters deve ser uma lista de tuplas (ano, trimestre)")
        
    caminho = os.path.abspath(sys.argv[0])
    base_url = "https://data.bls.gov/cew/data/api/{year}/{quarter}/industry/10.csv"
    data_dir = "data"
    arquivos_baixados = []

    # Cria diretório 'data/' se não existir
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Baixa os arquivos CSV
    for ano, trimestre in years_quarters:
        url = base_url.format(year=ano, quarter=trimestre)
        nome_arquivo = os.path.join(caminho, data_dir, f"{ano}_q{trimestre}.csv")

        try:
            print(f"Baixando {url}...")
            urllib.request.urlretrieve(url, nome_arquivo)
            arquivos_baixados.append(nome_arquivo)
        except Exception as e:
            print(f"Erro ao baixar {url}: {e}")

    # Ordena os arquivos por nome
    arquivos_baixados.sort()

    # Merge dos CSVs
    with open(output_file, "w", newline="", encoding="utf-8") as outfile:
        escritor = None
        for arq in arquivos_baixados:
            with open(arq, "r", encoding="utf-8") as infile:
                leitor = csv.reader(infile)
                cabecalho = next(leitor)
                if escritor is None:
                    escritor = csv.writer(outfile)
                    escritor.writerow(cabecalho)
                for linha in leitor:
                    escritor.writerow(linha)
            
    print(f"Arquivo mesclado salvo como: {output_file}")

# Teste principal
if __name__ == "__main__":
    combinacoes = [(2024, 1), (2024, 2), (2024, 3), (2024, 4)]
    download_and_merge(combinacoes, "bls_dados_concatenados.csv")


