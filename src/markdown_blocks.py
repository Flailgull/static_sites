import re 
from htmlnode import *
from leafnode import *
from parentnode import *
from inline_markdown import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line[1:].strip()
    raise ValueError("Needs at least one h1 header like '# Header'")

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    #check if this is a heading:
    if re.findall(r"#{1,6} .+", block):
        return block_type_heading
    #check for a code-block
    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    #check for a quote-block, unordered- and ordered-list
    is_quote = True
    is_unordered_list = True
    is_ordered_list = True
    line_number = 1
    lines = block.split("\n")
    for line in lines:
        if line[0] != ">":
            is_quote = False
        if line[0] != "*" and line[0] != "-":
            is_unordered_list = False
        ordered_list_line_start = str(line_number) + "."
        if line[0:len(ordered_list_line_start)] != ordered_list_line_start:
            is_ordered_list = False
        line_number += 1
        if not is_quote and not is_unordered_list and not is_ordered_list:
            break

    if is_quote:
        return block_type_quote
    if is_unordered_list:
        return block_type_unordered_list
    if is_ordered_list:
        return block_type_ordered_list
    return block_type_paragraph

def block_to_HTMLNode(block, block_type):
    if block_type == block_type_paragraph:
        return block_to_paragraph(block)
    if block_type == block_type_heading:
        return block_to_heading(block)
    if block_type == block_type_code:
        return block_to_code(block)
    if block_type == block_type_quote:
        return block_to_quote(block)
    if block_type == block_type_unordered_list:
        return block_to_unordered_list(block)
    if block_type == block_type_ordered_list:
        return block_to_ordered_list(block)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def block_to_paragraph(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def block_to_heading(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def block_to_code(block):
    text = block[3:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    parent = ParentNode("pre", [code])
    return parent

def block_to_quote(block):
    lines = block.split("\n")
    new_lines = list(map(lambda line: line[1:], lines))
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def block_to_unordered_list(block):
    lines = block.split("\n")
    inner_nodes = []
    for line in lines:
        text = line[1:].strip()
        children = text_to_children(text)
        inner_nodes.append(ParentNode("li", children))
    outer_node = ParentNode("ul", inner_nodes)
    return outer_node

def block_to_ordered_list(block):
    lines = block.split("\n")
    inner_nodes = []
    line_counter = 1
    for line in lines:
        text = line[len(f"{line_counter}."):].strip()
        children = text_to_children(text)
        inner_nodes.append(ParentNode("li", children))
        line_counter += 1
    outer_node = ParentNode("ol", inner_nodes)
    return outer_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    inner_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        node = block_to_HTMLNode(block, block_type)
        inner_nodes.append(node)
    parent = ParentNode("div", inner_nodes)
    return parent