import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("A", "bold")
        node2 = TextNode("B", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("A", "bold")
        node2 = TextNode("A", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_url(self):
        node = TextNode("A", "bold")
        node2 = TextNode("A", "bold", "random_url")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()