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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        image_tuples = extract_markdown_images(old_node.text)
        substrings = []
        post_image = old_node.text
        for image_tuple in image_tuples:
            pre_image, post_image = post_image.split(f"![{image_tuple[0]}]({image_tuple[1]})", 1)
            new_nodes.append(TextNode(pre_image, text_type_text))
            new_nodes.append(TextNode(image_tuple[0], text_type_image, image_tuple[1]))
        if post_image != "":
            new_nodes.append(TextNode(post_image, text_type_text))
            
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        link_tuples = extract_markdown_links(old_node.text)
        substrings = []
        post_link = old_node.text
        for link_tuple in link_tuples:
            pre_link, post_link = post_link.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)
            new_nodes.append(TextNode(pre_link, text_type_text))
            new_nodes.append(TextNode(link_tuple[0], text_type_link, link_tuple[1]))
        if post_link != "":
            new_nodes.append(TextNode(post_link, text_type_text))
            
            
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

