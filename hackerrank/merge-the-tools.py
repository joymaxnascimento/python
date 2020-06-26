"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/merge-the-tools
"""


def merge_the_tools(string, k):
    for i in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in i if c not in d]))
