import unittest

from textnode import *
from inline_markdown import *

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


    def test_extract_markdown_images(self):
        self.maxDiff = None
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

    def test_extract_markdown_links(self):
        self.maxDiff = None
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()