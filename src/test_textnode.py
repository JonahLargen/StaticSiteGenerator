import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_properties_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual(node.text, node2.text)
        self.assertEqual(node.text_type, node2.text_type)
        self.assertEqual(node.url, node2.url)
        
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a second text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_text_to_html_text(self):
        text_node = TextNode("hello", TextType.TEXT)
        html_node = LeafNode(None, "hello")
        html_node_2 = text_node.to_html_node()
        self.assertEqual(html_node, html_node_2)
        
    def test_text_to_html_bold(self):
        text_node = TextNode("hello", TextType.BOLD)
        html_node = LeafNode("b", "hello")
        html_node_2 = text_node.to_html_node()
        self.assertEqual(html_node, html_node_2)
        
    def test_text_to_html_italic(self):
        text_node = TextNode("hello", TextType.ITALIC)
        html_node = LeafNode("i", "hello")
        html_node_2 = text_node.to_html_node()
        self.assertEqual(html_node, html_node_2)

if __name__ == "__main__":
    unittest.main()