import unittest

from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "hello world")
        node2 = LeafNode("p", "hello world")
        self.assertEqual(node, node2)
        
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html = node.to_html()
        self.assertEqual(html, "<p>This is a paragraph of text.</p>")
        
    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = node.to_html()
        self.assertEqual(html, "<a href=\"https://www.google.com\">Click me!</a>")
        
    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a block of text.")
        html = node.to_html()
        self.assertEqual(html, "This is a block of text.")
        
    def test_to_html_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()