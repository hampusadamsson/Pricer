from unittest import TestCase
from data_manager import save, load


class TestSave(TestCase):
    save("2019-01-01", "test_item", "onoff", 23)
    pass


class TestLoad(TestCase):
    load()
    pass


