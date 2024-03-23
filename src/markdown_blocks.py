import re 
from htmlnode import *
from leafnode import *
from parentnode import *

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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

def block_to_paragraph(block):
    return LeafNode("p", block)

def block_to_heading(block):
    if block.startswith("######"):
        return LeafNode("h6", block[7:])
    if block.startswith("#####"):
        return LeafNode("h5", block[6:])
    if block.startswith("####"):
        return LeafNode("h4", block[5:])
    if block.startswith("###"):
        return LeafNode("h3", block[4:])
    if block.startswith("##"):
        return LeafNode("h2", block[3:])
    if block.startswith("#"):
        return LeafNode("h1", block[2:])

def block_to_code(block):
    inner_node = LeafNode("code", block[3:-3])
    outer_node = ParentNode("pre", [inner_node])
    return outer_node

def block_to_quote(block):
    lines = block.split("\n")
    new_lines = list(map(lambda line: line[1:], lines))
    text = "\n".join(new_lines)
    return LeafNode("blockquote", text)

def block_to_unordered_list(block):
    lines = block.split("\n")
    inner_nodes = []
    for line in lines:
        inner_nodes.append(LeafNode("li", line[1:].strip()))
    outer_node = ParentNode("ul", inner_nodes)
    return outer_node

def block_to_ordered_list(block):
    lines = block.split("\n")
    inner_nodes = []
    line_counter = 1
    for line in lines:
        inner_nodes.append(LeafNode("li", line[len(f"{line_counter}."):].strip()))
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