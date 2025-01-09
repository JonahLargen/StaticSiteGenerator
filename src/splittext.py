from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    
    split_nodes = split_nodes_delimiter([initial_node], '**', TextType.BOLD)
    split_nodes = split_nodes_delimiter(split_nodes, '*', TextType.ITALIC)
    split_nodes = split_nodes_delimiter(split_nodes, '`', TextType.CODE)
    split_nodes = split_nodes_image(split_nodes)
    split_nodes = split_nodes_link(split_nodes)
    
    return split_nodes

def markdown_to_blocks(markdown):
    texts = markdown.split('\n\n')
    texts = list(map(lambda x: x.strip(), texts))
    texts = list(filter(lambda x: len(x) > 0, texts))
    return texts