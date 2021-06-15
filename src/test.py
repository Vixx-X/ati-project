"""
Main file for testing procedures
"""

import unittest

import app


class TestHello(unittest.TestCase):
    """
    Test the main hello page
    """
    def setUp(self):
        """
        Set up test
        """
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        """
        Test procedure
        """
        rv = self.app.get("/")
        self.assertEqual(rv.status, "200 OK")
        self.assertEqual(rv.data, b"Hello World!\n")


if __name__ == "__main__":
    unittest.main()
