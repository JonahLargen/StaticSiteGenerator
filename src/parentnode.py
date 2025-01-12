from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        HtmlNode.__init__(self, tag, None, children, props)
        
    def to_html(self):
        if (self.tag is None):
            raise ValueError("Parent Node must have a tag")
        if (self.children is None):
            raise ValueError("Parent Node must children")
        return f"<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"