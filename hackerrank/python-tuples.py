"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/python-tuples
"""
n = int(input())
tupla = tuple(map(int, input().split()))
print(hash(tupla))
