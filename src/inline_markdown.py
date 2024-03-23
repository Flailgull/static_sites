from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            substrings = node.text.split(delimiter)
            if len(substrings) % 2 == 0:
                raise ValueError("Closing delimiter not found")
            else:
                is_text = True
                for substring in substrings:
                    if is_text:
                        new_nodes.append(TextNode(substring, text_type_text))
                        is_text = False
                    else:
                        new_nodes.append(TextNode(substring, text_type))
                        is_text = True
        
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)