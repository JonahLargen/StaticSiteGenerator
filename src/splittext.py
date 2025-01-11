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
    parent_node = HtmlNode(tag="div",children=nodes)
    return parent_node
            
def text_to_html_node(block):
    block_type = block_to_block_type(block)
    if (block_type == "heading"):
        for i in range(1, 7):
            if block.startswith('#' * i):
                text = block[i + 1:]
                return HtmlNode(tag=f"h{i}",value=text)
    elif (block_type == "code"):
        text = "\n".join(block.split('\n')[1:-1])
        inner_node = HtmlNode(tag="code",value=text)
        return HtmlNode(tag="pre",children=[inner_node])
    elif (block_type == "quote"):
        text = "\n".join(map(lambda s: s[1:], block.split("\n")))
        return HtmlNode(tag="blockquote",value=text)
    elif (block_type == "unordered_list"):
        texts = list(map(lambda s: HtmlNode(tag="li",value=s[2:]), block.split("\n")))
        return HtmlNode(tag="ul",children=texts)
    elif (block_type == "ordered_list"):
        texts = list(map(lambda s: HtmlNode(tag="li",value=s[1][(len(str(s[0])) + 2):]), enumerate(block.split("\n"), start=1)))
        return HtmlNode(tag="ol",children=texts)
    elif (block_type == "paragraph"):
        text_nodes = text_to_textnodes(block)
        html_nodes = list(map(lambda t: t.to_html_node(), text_nodes))
        return HtmlNode(tag="p",children=html_nodes)
    else:
        raise ValueError(f"Unknown block type: {block_type}")