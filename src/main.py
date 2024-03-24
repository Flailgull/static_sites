import os
import shutil
from textnode import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from markdown_blocks import *


def move_stuff(srcdir, destdir):
    #noch nicht fertig: das muss noch rekursiv, die dest-dir muss geleert werden (VORSICHT!) und die ordner müssen auch rüber

    #abort conditions
    if srcdir is None or srcdir == "":
        return
    if not os.path.exists(srcdir):
        raise ValueError(f"path {srcdir} does not exist")
    
    if destdir is None or destdir == "":
        return
    if not os.path.exists(destdir):
        raise ValueError(f"path {destdir} does not exist")
    
    #remove the current content of the src-dir
    shutil.rmtree(destdir)
    os.mkdir(destdir)

    #actual algorithm
    move_stuff_r(srcdir, destdir)

def move_stuff_r(srcdir, destdir):
    list_of_stuff = os.listdir(srcdir)
    for stuff in list_of_stuff:
        entity_name = os.path.join(srcdir, stuff)
        #if it's a file
        if os.path.isfile(entity_name):
            shutil.copy(entity_name, os.path.join(destdir, stuff))
            print(f"copied {entity_name} to {os.path.join(destdir, stuff)}")
        #if it's a directory
        else:
            new_dest = os.path.join(destdir, stuff)
            os.mkdir(new_dest)
            print(f"created folder {new_dest}")
            move_stuff_r(entity_name, new_dest)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path) or not os.path.isabs(from_path):
        from_path = os.path.join(os.getcwd(), from_path)

    if not os.path.exists(template_path) or not os.path.isabs(template_path):
        template_path = os.path.join(os.getcwd(), template_path)

    if not os.path.isabs(dest_path):
        dest_path = os.path.join(os.getcwd(), dest_path)

    markdown_file =  open(from_path)
    markdown_contents = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    template_contents = template_file.read()
    template_file.close()
    
    html = markdown_to_html_node(markdown_contents).to_html()
    title = extract_title(markdown_contents)
    html_contents = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html)

    path = os.path.dirname(dest_path)
    if not os.path.exists(path):        
        os.mkdir(path)
    
    dest_file = open(dest_path, "w")
    dest_file.write(html_contents)
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_of_stuff = os.listdir(dir_path_content)
    for stuff in list_of_stuff:
        abs_path = os.path.join(dir_path_content, stuff)
        abs_dest = os.path.join(dest_dir_path, stuff)
        if os.path.isfile(abs_path):
            if abs_path.endswith(".md"):
                abs_dest = os.path.splitext(abs_dest)[0] + ".html"
                generate_page(abs_path, template_path, abs_dest)
        else:
            generate_pages_recursive(abs_path, template_path, abs_dest)

def main():
    #open(os.path.join(os.getcwd(),  "src/main.py"))
    cwd = os.getcwd()
    move_stuff(os.path.join(cwd, "static"), os.path.join(cwd, "public"))
    generate_pages_recursive(os.path.join(cwd, "content"), os.path.join(cwd, "template.html"), os.path.join(cwd, "public"))



main()