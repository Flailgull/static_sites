import re 

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

