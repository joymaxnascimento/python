"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/py-if-else
"""

n = int(input('Digite um número inteiro:\n'))
if 2 <= n <= 5 and n % 2 == 0:
    print('Not Weird')
elif 6 <= n <= 20 and n % 2 == 0:
    print('Weird')
elif 20 > n % 2 == 0:
    print('Not Weird')
else:
    print('Weird')
