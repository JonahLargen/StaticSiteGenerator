from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        HtmlNode.__init__(self, tag, value, None, props)
        
    def to_html(self):
        if (self.value is None):
            raise ValueError("All leaf nodes must have a value")
        if (self.tag is None):
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"