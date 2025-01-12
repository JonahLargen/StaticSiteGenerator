import unittest

from splittext import text_to_textnodes, markdown_to_blocks, block_to_block_type, markdown_to_html_node, extract_title
from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode

class TestSplitText(unittest.TestCase):
    def test_splittext_eq(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        nodes2 = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, nodes2)
        
    def test_markdown_to_blocks_eq(self):
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        blocks = markdown_to_blocks(markdown)
        blocks2 = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            '''* This is the first list item in a list block
* This is a list item
* This is another list item'''
        ]
        self.assertEqual(blocks, blocks2)
        
    def test_markdown_to_blocks_extra_eq(self):
        markdown = ''' # This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it. 


* This is the first list item in a list block
* This is a list item
* This is another list item'''
        blocks = markdown_to_blocks(markdown)
        blocks2 = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            '''* This is the first list item in a list block
* This is a list item
* This is another list item'''
        ]
        self.assertEqual(blocks, blocks2)
        
    def test_block_to_block_type_heading(self):
        types = [
            block_to_block_type("# hello"),
            block_to_block_type("## hello"),
            block_to_block_type("### hello"),
            block_to_block_type("#### hello"),
            block_to_block_type("##### hello"),
            block_to_block_type("###### hello")
        ]
        for type in types:
            self.assertEqual(type, 'heading')
            
    def test_block_to_block_type_code(self):
        text = "```\ncode\n```"
        type = block_to_block_type(text)
        self.assertEqual(type, 'code')
        
    def test_block_to_block_type_quote(self):
        type = block_to_block_type(">hello\n>world")
        self.assertEqual(type, 'quote')
        
    def test_block_to_block_type_unordered_list(self):
        type = block_to_block_type("* hello\n- world")
        self.assertEqual(type, 'unordered_list')
        
    def test_block_to_block_type_ordered_list(self):
        type = block_to_block_type("1. hello\n2. world")
        self.assertEqual(type, 'ordered_list')
        
    def test_block_to_block_type_ordered_paragraph(self):
        types = [
            block_to_block_type("hello world"),
            block_to_block_type("#hello world"),
            block_to_block_type("####### hello world"),
            block_to_block_type(">hello\nworld"),
            block_to_block_type("*hello\n- world"),
            block_to_block_type("1. hello\n3. world")
        ]
        for type in types:
            self.assertEqual(type, 'paragraph')
            
    def test_markdown_to_html_node(self):
        markdown = '''# Header

Paragraph

- List Item **A**
- List Item B

1. List Item 1
2. List Item 2

[link](somewhere)

![image](something)

*italics*

**bold**

`code`

```
code block
```

> quote block'''
        html = markdown_to_html_node(markdown)
        html2 = ParentNode(tag="div",children=[
            ParentNode(tag="h1",children=[
                LeafNode(tag=None,value="Header")
            ]),
            ParentNode(tag="p",children=[
                LeafNode(tag=None,value="Paragraph")
            ]),
            ParentNode(tag="ul",children=[
                ParentNode(tag="li",children=[
                    LeafNode(tag=None,value="List Item "),
                    LeafNode(tag="b",value="A")
                ]),
                ParentNode(tag="li",children=[
                    LeafNode(tag=None,value="List Item B")
                ])
            ]),
            ParentNode(tag="ol",children=[
                ParentNode(tag="li",children=[
                    LeafNode(tag=None,value="List Item 1")
                ]),
                ParentNode(tag="li",children=[
                    LeafNode(tag=None,value="List Item 2")
                ])
            ]),
            ParentNode(tag="p",children=[
                LeafNode(tag="a",value="link",props={"href":"somewhere"})
            ]),
            ParentNode(tag="p",children=[
                LeafNode(tag="img",value="",props={"src":"something","alt":"image"})
            ]),
            ParentNode(tag="p",children=[
                LeafNode(tag="i",value="italics")
            ]),
            ParentNode(tag="p",children=[
                LeafNode(tag="b",value="bold")
            ]),
            ParentNode(tag="p",children=[
                LeafNode(tag="code",value="code")
            ]),
            ParentNode(tag="pre",children=[
                ParentNode(tag="code",children=[
                    LeafNode(tag=None,value="code block")
                ])
            ]),
            ParentNode(tag="blockquote",children=[
                LeafNode(tag=None,value="quote block")
            ])
        ])
        self.assertEqual(html, html2)
        
    def test_extract_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title, 'Hello')