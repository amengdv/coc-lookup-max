import unittest

from src.csvhandler import get_col_at

class TestCsv(unittest.TestCase):

    def test_get_col_at(self):

        csv1 = """TOWNHALL,7,8
Canon,7,8
Test,7,8
"""

        self.assertEqual(
            get_col_at(7, csv1),
"""TOWNHALL 7
Canon: 7
Test: 7
"""
        )
