import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        child_nodes = [HtmlNode("p", "goodbye world")]
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HtmlNode("p", "hello world", child_nodes, props)
        node2 = HtmlNode("p", "hello world", child_nodes, props)
        self.assertEqual(node, node2)
        
    def test_default_none(self):
        node = HtmlNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_prop_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        node = HtmlNode(props=props)
        html = node.props_to_html()
        self.assertEqual(html, " href=\"https://www.google.com\" target=\"_blank\"")