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
        #if it's a directory
        else:
            new_dest = os.path.join(destdir, stuff)
            os.mkdir(new_dest)
            move_stuff_r(entity_name, new_dest)

def main():
    test = TextNode("text", "text_type", "url")
    cwd = os.getcwd()
    move_stuff(os.path.join(cwd, "static"), os.path.join(cwd, "public"))



main()