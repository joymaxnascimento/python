"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/python-mutations
"""


def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string
