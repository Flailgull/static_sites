import unittest

from parentnode import (
    ParentNode
)

from leafnode import(
    LeafNode
)

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        self.maxDiff = None
        leaf = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("b", "Some bold text")

        parent = ParentNode("a", [leaf, leaf2], {"class": "parent", "href": "http://some_url.com"})
        expected_text = "ParentNode(tag - a, children - [LeafNode(tag - p, value - This is a paragraph of text., props - None), LeafNode(tag - b, value - Some bold text, props - None)], props - {'class': 'parent', 'href': 'http://some_url.com'})"
        node_text = parent.__repr__()
        self.assertEqual(node_text, expected_text)
    
    def test_value_error_tag(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("b", "Some bold text")
        expected_error = ValueError("ParentNode needs a tag")

        parent = ParentNode(None, [leaf, leaf2], {"class": "parent", "href": "http://some_url.com"})
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(context.exception.__repr__(), expected_error.__repr__())
        
    def test_value_error_children(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("b", "Some bold text")
        expected_error = ValueError("ParentNode needs children")

        parent = ParentNode("a", None, {"class": "parent", "href": "http://some_url.com"})
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(context.exception.__repr__(), expected_error.__repr__())

    #stuff they tested for in the solution:
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()