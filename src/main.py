from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from block_markdown import *


def main():
    test = TextNode("text", "text_type", "url")
    print(test)


main()