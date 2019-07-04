from unittest import TestCase

from analyzer import analyze


class TestAnalyze(TestCase):
    data = analyze()
    print(data)
    pass
