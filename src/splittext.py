from parentnode import ParentNode
from htmlnode import HtmlNode
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
    lines = markdown.split('\n')
    for i in range(1, 7):
        if markdown.startswith('#' * i + ' '):
            return "heading"
    if (len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```")):
        return "code"
    if (all(map(lambda line: line.startswith('>'), lines))):
        return "quote"
    if (all(map(lambda line: line.startswith('* ') or line.startswith('- '), lines))):
        return "unordered_list"
    if (all(map(lambda x: x[1].startswith(f"{int(x[0]) + 1}. "), enumerate(lines)))):
        return "ordered_list"
    return "paragraph"

def markdown_to_html_node(markdown):
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        node = text_to_html_node(block)
        nodes.append(node)
    parent_node = ParentNode(tag="div",children=nodes)
    return parent_node
            
def text_to_html_node(block):
    block_type = block_to_block_type(block)
    if (block_type == "heading"):
        for i in range(1, 7):
            if block.startswith('#' * i):
                text = block[i + 1:]
                return ParentNode(tag=f"h{i}",children=text_to_children(text))
    elif (block_type == "code"):
        text = "\n".join(block.split('\n')[1:-1])
        inner_node = ParentNode(tag="code",children=text_to_children(text))
        return ParentNode(tag="pre",children=[inner_node])
    elif (block_type == "quote"):
        text = "\n".join(map(lambda s: s[2:], block.split("\n")))
        return ParentNode(tag="blockquote",children=text_to_children(text))
    elif (block_type == "unordered_list"):
        children = list(map(lambda s: ParentNode(tag="li",children=text_to_children(s[2:])), block.split("\n")))
        return ParentNode(tag="ul",children=children)
    elif (block_type == "ordered_list"):
        children = list(map(lambda s: ParentNode(tag="li",children=text_to_children(s[1][(len(str(s[0])) + 2):])), enumerate(block.split("\n"), start=1)))
        return ParentNode(tag="ol",children=children)
    elif (block_type == "paragraph"):
        return ParentNode(tag="p",children=text_to_children(block))
    else:
        raise ValueError(f"Unknown block type: {block_type}")
   
def text_to_children(text):
    return list(map(lambda t: t.to_html_node(), text_to_textnodes(text)))
    
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == "heading" and block.startswith('# '):
            return block[2:]
    raise Exception('No title found')