"""
https://www.hackerrank.com/contests/linguagens-de-programacao-para-ciencia-de-dados/challenges/python-string-split-and-join
"""


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
