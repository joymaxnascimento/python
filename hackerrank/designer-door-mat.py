"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/designer-door-mat
"""

linha, coluna = map(int, input().split())
padrao = [('.|.' * (2 * i + 1)).center(coluna, '-') for i in range(linha // 2)]
print('\n'.join(padrao + ['WELCOME'.center(coluna, '-')] + padrao[::-1]))
