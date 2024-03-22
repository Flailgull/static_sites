import unittest

from textnode import *

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter_1(self):
        self.maxDiff = None
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected_result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_split_nodes_delimiter_2(self):
        self.maxDiff = None
        node = TextNode("code block", text_type_code)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected_result = [
            TextNode("code block", text_type_code)
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_split_nodes_delimiter_error(self):
        self.maxDiff = None
        node = TextNode("This is text with a `code block word", text_type_text)
        expected_error = ValueError("Closing delimiter not found")
        with self.assertRaises(ValueError) as context:
            new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        
        self.assertEqual(context.exception.__repr__(), expected_error.__repr__())

    def test_split_nodes_delimiter_error_2(self):
        self.maxDiff = None
        node = TextNode("This is `text with a `code block` word", text_type_text)
        expected_error = ValueError("Closing delimiter not found")
        with self.assertRaises(ValueError) as context:
            new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        
        self.assertEqual(context.exception.__repr__(), expected_error.__repr__())

if __name__ == "__main__":
    unittest.main()