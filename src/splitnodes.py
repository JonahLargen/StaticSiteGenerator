import re

from textnode import TextType, TextNode
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if (old_node.text_type != TextType.TEXT):
            new_nodes.append(old_node)
            continue
        
        sections = old_node.text.split(delimiter)
        
        if (len(sections) % 2 == 0):
            raise ValueError("Invalid markdown syntax, all markdown that is opened must be closed by a matching tag")
        
        text_field = True
        
        for section in sections:
            if (section == ""):
                continue
            
            if (text_field):
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))
                
            text_field = not text_field

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        working_text = old_node.text
        links = extract_markdown_images(working_text)
        
        for link in links:
            link_text = link[0]
            link_link = link[1]
            sections = working_text.split(f"![{link_text}]({link_link})", 1)
            
            if (len(sections) != 2):
                raise ValueError("Invalid markdown, image section not closed")
            
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.IMAGE, link_link))
            working_text = sections[1]
    
        new_nodes.append(TextNode(working_text, TextType.TEXT))
    
    return list(filter(lambda x: len(x.text) > 0, new_nodes))

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        working_text = old_node.text
        links = extract_markdown_links(working_text)
        
        for link in links:
            link_text = link[0]
            link_link = link[1]
            sections = working_text.split(f"[{link_text}]({link_link})", 1)
            
            if (len(sections) != 2):
                raise ValueError("Invalid markdown, link section not closed")
            
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_link))
            working_text = sections[1]
    
        new_nodes.append(TextNode(working_text, TextType.TEXT))
    
    return list(filter(lambda x: len(x.text) > 0, new_nodes))