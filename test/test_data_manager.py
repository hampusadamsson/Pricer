from unittest import TestCase
from data_manager import save, load, get_vendor_item_price


class TestSave(TestCase):
    # save("2019-01-01", "test_item", "onoff", 23)
    pass


class TestLoad(TestCase):
    # load()
    pass


class TestLoadSpecific(TestCase):
    res = get_vendor_item_price("2019-07-04", "pgw")
    print(res)
    pass

