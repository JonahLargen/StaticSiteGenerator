class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        front_tag = f"<{self.tag}{self.props_to_html()}>"
        back_tag = f"</{self.tag}>"
        
        if (self.children is not None):
            child_html = "".join(map(lambda child: child.to_html(), self.children))
            return f"{front_tag}{child_html}{back_tag}"
        
        return f"{front_tag}{self.value}{back_tag}"
    
    def props_to_html(self):
        if (self.props is None):
            return ""
        
        return f" {" ".join(map(lambda p: f"{p[0]}=\"{p[1]}\"", self.props.items()))}"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"