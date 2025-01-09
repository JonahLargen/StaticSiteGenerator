import unittest

from splittext import text_to_textnodes, markdown_to_blocks
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