import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node, node2)
        
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        html = node.to_html()
        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        
    def test_to_html_multiple_levels(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text")
                    ]
                )
            ]
        )
        html = node.to_html()
        self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text</p></p>")
        
    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_to_html_no_tag(self):
        node = ParentNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_to_html_empty_children(self):
        node = ParentNode(
            "p",
            [
                
            ]
        )
        html = node.to_html()
        self.assertEqual(html, "<p></p>")