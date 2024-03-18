from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def __repr__(self) -> str:
        return f"LeafNode(tag - {self.tag}, value - {self.value}, props - {self.props})"

    def to_html(self) -> str:
        if value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"