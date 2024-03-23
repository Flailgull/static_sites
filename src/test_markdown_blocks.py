import unittest
from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type(self):
        heading_paragraph = "### Testheading"
        code_block = "```Codeblock stuf code bla```"
        code_block_wrong_end = "```Codeblock stuf code bla``` asdkjasd"
        code_block_wrong_start = "asdadasd```Codeblock stuf code bla```"
        quote_block = ">Testquote"
        quote_block_multiline = ">Line1\n>Line2\n>Line3"
        quote_block_multiline_wrong = ">Line1\nLine2\nLine3"
        unordered_list_block = "* item\n- otheritem\n*last_item"
        ordered_list_block = "1.First Line\n2.Second Line\n3.Third Line"

        self.assertEqual(block_type_heading, block_to_block_type(heading_paragraph))
        self.assertEqual(block_type_code, block_to_block_type(code_block))
        self.assertEqual(block_type_paragraph, block_to_block_type(code_block_wrong_end))
        self.assertEqual(block_type_paragraph, block_to_block_type(code_block_wrong_start))
        self.assertEqual(block_type_quote, block_to_block_type(quote_block))
        self.assertEqual(block_type_quote, block_to_block_type(quote_block_multiline))
        self.assertEqual(block_type_paragraph, block_to_block_type(quote_block_multiline_wrong))
        self.assertEqual(block_type_unordered_list, block_to_block_type(unordered_list_block))
        self.assertEqual(block_type_ordered_list, block_to_block_type(ordered_list_block))

    def test_block_to_heading(self):
        heading_paragraph = "### Testheading"
        expected_node = ParentNode("h3", [
            LeafNode(None, "Testheading")
        ])
        actual_node = block_to_heading(heading_paragraph)

        self.assertEqual(expected_node, actual_node)

    def test_block_to_code(self):
        code_block = "```Codeblock stuf code bla```"
        
        expected_node = ParentNode("pre", [
            ParentNode("code", [LeafNode(None, "Codeblock stuf code bla")])
        ])
        actual_node = block_to_code(code_block)

        self.assertEqual(expected_node, actual_node)

    def test_block_to_quote(self):
        quote_block_multiline = ">Line1\n>Line2\n>Line3"

        expected_node = ParentNode("blockquote", [
            LeafNode(None, "Line1 Line2 Line3")
        ])
        actual_node = block_to_quote(quote_block_multiline)

        self.assertEqual(expected_node, actual_node)

    def test_block_to_unordered_list(self):
        self.maxDiff = None
        unordered_list_block = "*item\n*otheritem\n*last_item"

        expected_node = ParentNode("ul", [
            ParentNode("li", [LeafNode(None, "item")]),
            ParentNode("li", [LeafNode(None, "otheritem")]), 
            ParentNode("li", [LeafNode(None, "last_item")])
        ])
        actual_node = block_to_unordered_list(unordered_list_block)

        self.assertEqual(expected_node, actual_node)

    def test_block_to_ordered_list(self):
        self.maxDiff = None
        ordered_list_block = "1. item\n2. otheritem\n3. last_item"

        expected_node = ParentNode("ol", [
            ParentNode("li", [LeafNode(None, "item")]), 
            ParentNode("li", [LeafNode(None, "otheritem")]), 
            ParentNode("li", [LeafNode(None, "last_item")])
        ])
        actual_node = block_to_ordered_list(ordered_list_block)

        self.assertEqual(expected_node, actual_node)

    def test_markdown_to_html_node(self):
        self.maxDiff = None
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
* This is another list item"""
        expected_node = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "This is a heading")]),
            ParentNode("p", [
                LeafNode(None, "This is a paragraph of text. It has some "),
                LeafNode("b", "bold"),
                LeafNode(None, " and "),
                LeafNode("i", "italic"),
                LeafNode(None, " words inside of it.")
            ]),
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "This is a list item")]),
                ParentNode("li", [LeafNode(None,"This is another list item")])
            ])
        ])
        actual_node = markdown_to_html_node(markdown)

        self.assertEqual(expected_node, actual_node)

if __name__ == "__main__":
    unittest.main()