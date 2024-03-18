import unittest

from leafnode import (
    LeafNode
)

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_text = "LeafNode(tag - p, value - This is a paragraph of text., props - None)"
        node_text = node.__repr__()
        self.assertEqual(node_text, expected_text)

    def test_props_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.", {"class": "leaftest", "id": "testid"})
        expected_text = "<p class=\"leaftest\" id=\"testid\">This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_text)

if __name__ == "__main__":
    unittest.main()