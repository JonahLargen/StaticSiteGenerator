import unittest

from splittext import text_to_textnodes, markdown_to_blocks, block_to_block_type
from textnode import TextNode, TextType

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
        type = block_to_block_type("```hello world```")
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