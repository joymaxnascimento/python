"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/list-comprehensions
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
lista = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
print(lista)
