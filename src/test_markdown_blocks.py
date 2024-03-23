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
        ordered_list_block = "1.First Line\n2.\Second Line\n3.Third Line"

        self.assertEqual(block_type_heading, block_to_block_type(heading_paragraph))
        self.assertEqual(block_type_code, block_to_block_type(code_block))
        self.assertEqual(block_type_paragraph, block_to_block_type(code_block_wrong_end))
        self.assertEqual(block_type_paragraph, block_to_block_type(code_block_wrong_start))
        self.assertEqual(block_type_quote, block_to_block_type(quote_block))
        self.assertEqual(block_type_quote, block_to_block_type(quote_block_multiline))
        self.assertEqual(block_type_paragraph, block_to_block_type(quote_block_multiline_wrong))
        self.assertEqual(block_type_unordered_list, block_to_block_type(unordered_list_block))
        self.assertEqual(block_type_ordered_list, block_to_block_type(ordered_list_block))

if __name__ == "__main__":
    unittest.main()