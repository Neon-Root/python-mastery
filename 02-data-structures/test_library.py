import unittest
from unittest.mock import patch
from io import StringIO
from library import add_book, list_books


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = []  # fresh empty library before every test

    def test_add_book(self):
        add_book(self.library, "Born a Crime", "Trevor Noah", 2016, "9780399588174", True)
        self.assertEqual(len(self.library), 1)
        self.assertEqual(self.library[0]["title"], "Born a Crime")
        self.assertEqual(self.library[0]["isbn"], "9780399588174")

    def test_add_second_book(self):
        add_book(self.library, "Dune", "Frank Herbert", 1965, "111", False)
        add_book(self.library, "1984", "George Orwell", 1949, "222", True)
        self.assertEqual(len(self.library), 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_books_empty(self, mock_stdout):
        list_books(self.library)
        self.assertEqual(mock_stdout.getvalue(), "Library currently empty\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_list_books_populated(self, mock_stdout):
        add_book(self.library, "Born a Crime", "Trevor Noah", 2016, "9780399588174", True)
        add_book(self.library, "Analysis", "Tarens Tau", 2021, "9781234567897", False)

        list_books(self.library)

        printed_output = mock_stdout.getvalue()
        self.assertIn("'Born a Crime' by Trevor Noah in year 2016 - Status: In shelves", printed_output)
        self.assertIn("'Analysis' by Tarens Tau in year 2021 - Status: Borrowed", printed_output)


if __name__ == "__main__":
    unittest.main()