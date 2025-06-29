# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 13:47:05 2025

@author: jsampaio
"""
## Parte 1 - Listas

# Ex 1

def pares_e_impares(nums):
    """
    Separa uma lista de inteiros em duas listas:
    uma com os números pares e outra com os ímpares.
    """
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("A entrada deve ser uma lista de inteiros.")
    pares = []
    impares = []
    for num in nums:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

# Ex 2

def filtrar_por_tamanho(lista, k):
    """
    Filtra uma lista de strings, retornando apenas aquelas com comprimento maior que k.
    """
    if not isinstance(lista, list) or not all(isinstance(x, str) for x in lista) or not isinstance(k, int):
        raise ValueError("Entradas inválidas. Esperado: lista de strings e um inteiro.")   
    return [palavra for palavra in lista if len(palavra) > k]

# Ex 3

def rotate_tuple(tpl, n):
    """
    Rotaciona uma tupla n posições à direita.
    """
    if not isinstance(tpl, tuple) or not isinstance(n, int) or not tpl:
        raise ValueError("Entradas inválidas. Esperado: tupla não vazia e inteiro.")
    n = n % len(tpl) # Garante que n não seja maior que o tamanho da tupla
    return tpl[-n:] + tpl[:-n]

# Ex 4

def transpose(matrix):
    """
    Retorna a transposta de uma matriz representada como lista de listas.
    """
    if not matrix or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Entrada inválida. Esperado: matriz como lista de listas.")    
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise ValueError("Todas as linhas da matriz devem ter o mesmo tamanho.")
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Ex 5

def flatten(lst):
    """
    Achata uma lista aninhada de profundidade arbitrária.
    """
    if not isinstance(lst, list):
        raise ValueError("Entrada deve ser uma lista.")
    resultado = []
    for item in lst:
        if isinstance(item, list):
            resultado.extend(flatten(item))  # chamada recursiva para sublistas
        else:
            resultado.append(item)
    return resultado

# Testes 1

if __name__ == "__main__":
    print("Parte 1")    
    print('_'*40)
    print("Exercício 1")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares, impares = pares_e_impares(numeros)
        
    print("Lista:", numeros)
    print("Pares:", pares)
    print("Ímpares:", impares)
    print('_'*40)
    
    print("Exercício 2")
    
    k = 3
    palavras = ["Especialização", "FGV", "Emap", "é", "dificil"]
    resultado = filtrar_por_tamanho(palavras, k)
    
    print("Lista:", palavras)
    print(f"Palavras maiores que {k} letra(s):", resultado)
    print('_'*40)
    
    print("Exercício 3")
    
    n = 3
    t = (1, 2, 3, 4, 5)
    rotacionada = rotate_tuple(t, n)
    
    print("Tupla:", t)
    print(f"Tupla rotacionada {n} vez(es):", rotacionada)
    print('_'*40)
    
    print("Exercício 4")
    
    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    transposta = transpose(matriz)
    
    print("Matriz:", matriz)
    print("Matriz Transposta:", transposta)
    print('_'*40)
    
    print("Exercício 5")
    
    entrada = [1, [2, [3, 4], 5], 6]
    
    print("Lista de entrada:", entrada)
    print("Lista flettada:", flatten(entrada))
    print('_'*40)
    print('_'*40)

## Parte 2 - Dicionários

# Ex 1

def group_by(pairs):
    """
    Agrupa valores por chave a partir de uma lista de tuplas (chave, valor).
    """
    resultado = {}
    for chave, valor in pairs:
        if chave not in resultado:
            resultado[chave] = []
        resultado[chave].append(valor)
    return resultado

# Ex 2

def invert_map(d):
    """
    Inverte chaves e valores de um dicionário com valores únicos.
    """
    if any(isinstance(value, (list, tuple, set)) and len(value) != 1 for value in d.values()):
        raise ValueError("Cada chave deve conter exatamente um único valor.")
    return {value: key for key, value in d.items()}

# Ex 3

def indices_of(lst):
    """
    Retorna um dicionário com os índices de cada valor de uma lista.
    """
    resultado = {}
    for i, valor in enumerate(lst):
        if valor not in resultado:
            resultado[valor] = []
        resultado[valor].append(i)
    return resultado

# Ex 4

def merge_dicts(dicts):
    """
    Mescla uma lista de dicionários somando valores de chaves repetidas.
    """
    resultado = {}
    for d in dicts:
        for chave, valor in d.items():
            if chave in resultado:
                resultado[chave] += valor
            else:
                resultado[chave] = valor
    return resultado

# Ex 5

def conta_digitos(n):
    """
    Conta a frequência de cada dígito de 0 a 9 na representação decimal de um número inteiro.
    O resultado sempre contém as chaves de 0 a 9, mesmo que algum dígito não apareça.
    """
    if not isinstance(n, int):
        raise ValueError("A entrada deve ser um número inteiro.")

    resultado = {i: 0 for i in range(10)}  # inicializa todos os dígitos com 0

    for d in str(abs(n)):
        dig = int(d)
        resultado[dig] += 1

    return resultado

# Testes 2

if __name__ == "__main__":

    print("Parte 2 - Dicionários")
    print('_'*40)
    print("Exercício 1")
    
    dados = [("A", 1), ("B", 1), ("C", 3), ("A", 4)]
    agrupado = group_by(dados)
    
    print("Dados:", dados)
    print("Dados agrupados:", agrupado)
    print('_'*40)
    
    print("Exercício 2")
    
    d = {'a': 1, 'b': 2, 'c': 3}
    invertido = invert_map(d)
    
    print("Dicionários iniciais:", d)
    print("Dicionários invertidos:", invertido)
    print('_'*40)
    
    print("Exercício 3")
    
    entrada = ['a', 'b', 'a', 'c', 'b']
    
    print("Lista:", entrada)
    print("Indices da lista:", indices_of(entrada))
    print('_'*40)
    
    print("Exercício 4")
    
    entrada = [{"A": 1, "B": 1, "C": 3}, {"A": 4, "B": -4, "D": 2}]
    
    print("Lista de dicionários:", entrada)
    print("Dicionário unico somado:", merge_dicts(entrada))
    print('_'*40)
    
    print("Exercício 5")
    
    n = -1203401
    
    print("Número:", n)
    print("Frequencia por dígito:", conta_digitos(n))
    print('_'*40)

## Parte 3 - Desafios de Fuções

# Ex 1

def count_anagrams(words):
    """
    Agrupa anagramas com base nas letras ordenadas.
    """
    resultado = {}
    for palavra in words:
        chave = ''.join(sorted(palavra))
        if chave not in resultado:
            resultado[chave] = []
        resultado[chave].append(palavra)
    return resultado

# Ex 2

def parse_csv(text, sep=','):
    """
    Faz parsing de um texto CSV e retorna um dicionário de listas por coluna.
    """
    linhas = [linha.strip() for linha in text.strip().split('\n') if linha.strip()]
    cabecalho = linhas[0].split(sep)
    dados = {coluna: [] for coluna in cabecalho}
    for linha in linhas[1:]:
        valores = linha.split(sep)
        for i, valor in enumerate(valores):
            valor = valor.strip()
            try:
                valor = int(valor)
            except ValueError:
                try:
                    valor = float(valor)
                except ValueError:
                    pass
            dados[cabecalho[i]].append(valor)
    return dados

# Ex 3

def validar_sudoku(tabuleiro):
    """
    Valida se um tabuleiro 9x9 de Sudoku é válido (sem repetições nas linhas, colunas e blocos).
    """
    def sem_repeticoes(valores):
        numeros = [v for v in valores if v != 0]
        return len(numeros) == len(set(numeros))
    
    # Verificar linhas
    for linha in tabuleiro:
        if not sem_repeticoes(linha):
            return False
    
    # Verificar colunas
    for col in range(9):
        if not sem_repeticoes([tabuleiro[lin][col] for lin in range(9)]):
            return False
    
    # Verificar blocos 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloco = [tabuleiro[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not sem_repeticoes(bloco):
                return False

    return True

# Testes 3

if __name__ == "__main__":

    print("Parte 3 - Desafios de Fuções")
    print('_'*40)
    print("Exercício 1")
    
    palavras = ["bolo", "lobo", "gato", "toga", "amor", "roma"]
    
    print("Palavras:", palavras)
    print("Anagramas:", count_anagrams(palavras))
    print('_'*40)
    
    print("Exercício 2")
    
    texto = """
    Altura,Nome,Idade
    177,Pedro,21
    191,Carlos,33
    169,Alice,23
    """
    
    resultado = parse_csv(texto)
    
    print("Texto:", texto)
    print("Cabeçalhos:", resultado)
    print('_'*40)
    
    print("Exercício 3")
    
    tabuleiro_valido = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print(validar_sudoku(tabuleiro_valido))  # True


