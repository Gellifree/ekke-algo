import unittest
from analyzer.menu import MenuDrawer
import sys
from io import StringIO

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.original_stdout = sys.stdout
        self.original_stdin = sys.stdin

    def tearDown(self):
        sys.stdout = self.original_stdout
        sys.stdin = self.original_stdin

    def test_menu_draw_negative_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("-1")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, -2, "Expected output for input '-1' is -2")

    def test_menu_draw_empty_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO(" ")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, -3, "Expected output for empty input is -3")

    def test_menu_draw_zero_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("0")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, 0, "Expected output for input '0' is 0")

    def test_menu_draw_out_of_range_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("99")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, -2, "Expected output for input '99' is -2")

    def test_menu_draw_unknown_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("unknown")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, -3, "Expected output for input 'unknown' is -3")

    def test_menu_draw_quit_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("Q")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, -1, "Expected output for input 'Q' is -1")

    def test_menu_draw_lowercase_quit_input(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("q")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, -1, "Expected output for input 'q' is -1")

    def test_menu_draw_valid_index(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("1")
        answer = MenuDrawer.draw(['menu 1', 'menu 2'])
        self.assertEqual(answer, 1, "Expected output for input '1' is 1")

    def test_menu_draw_exit_option(self):
        sys.stdout = StringIO("")
        sys.stdin = StringIO("0")
        answer = MenuDrawer.draw(['Kilépés', 'menu 2'])
        self.assertEqual(answer, -1, "Expected output for input '0' with 'Kilépés' is -1")