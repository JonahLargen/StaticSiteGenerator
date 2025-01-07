import unittest

from splitnodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes_2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_2)
        
    def test_code_2(self):
        node = TextNode("This is text with a `code block` word and another `code block 2` word!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes_2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and another ", TextType.TEXT),
            TextNode("code block 2", TextType.CODE),
            TextNode(" word!", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_2)
        
    def test_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        new_nodes_2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_2)
        
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes_2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, new_nodes_2)
        
    def test_error(self):
        node = TextNode("This is text with a bad **bold word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
            
    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        new_nodes_2 = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(new_nodes, new_nodes_2)
        
    def test_split_image(self):
        node = TextNode(
            "This is text with a image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        new_nodes_2 = [
            TextNode("This is text with a image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(new_nodes, new_nodes_2)