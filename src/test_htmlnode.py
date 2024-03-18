import unittest

from htmlnode import (
    HTMLNode
)

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("tag", "value", "children", "props")
        expected_text = "HTMLNode(tag - tag, value - value, children - children, props - props)"
        node_text = node.__repr__()
        self.assertEqual(node_text, expected_text)

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", "children", {"dummy": "dummy_value", "dummy2": "dummy2_value"})
        expected_text = "dummy=\"dummy_value\" dummy2=\"dummy2_value\""
        self.assertEqual(node.props_to_html(), expected_text)

    def test_to_html_not_implemented(self):
        node =  HTMLNode("tag", "value", "children", {"dummy": "dummy_value", "dummy2": "dummy2_value"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_none(self):
        node = HTMLNode("tag", "value", "children", None)
        expected_text = ""
        self.assertEqual(node.props_to_html(), expected_text)

if __name__ == "__main__":
    unittest.main()