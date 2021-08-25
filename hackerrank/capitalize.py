"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/capitalize
"""


def solve(s):
    return ' '.join(s.capitalize() for s in s.split(' '))
