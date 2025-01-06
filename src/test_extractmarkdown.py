import unittest

from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        images = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        images_2 = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(images, images_2)
        
    def test_extract_links(self):
        links = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        links_2 = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(links, links_2)
        
    def test_extract_none(self):
        text = "This is text with nothing"
        images = extract_markdown_images(text)
        links = extract_markdown_links(text)
        self.assertEqual(images, [])
        self.assertEqual(links, [])