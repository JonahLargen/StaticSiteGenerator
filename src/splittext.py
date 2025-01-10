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

def block_to_block_type(markdown):
    for i in range(1, 7):
        if markdown.startswith('#' * i + ' '):
            return "heading"
    if (markdown.startswith('```') and markdown.endswith('```')):
        return "code"
    lines = markdown.split('\n')
    if (all(map(lambda line: line.startswith('>'), lines))):
        return "quote"
    if (all(map(lambda line: line.startswith('* ') or line.startswith('- '), lines))):
        return "unordered_list"
    if (all(map(lambda x: x[1].startswith(f"{int(x[0]) + 1}. "), enumerate(lines)))):
        return "ordered_list"
    return "paragraph"
