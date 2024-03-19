from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)

    def __repr__(self) -> str:
        inner_text = ""
        for node in self.children:
            inner_text += ", " + node.__repr__();
        return f"ParentNode(tag - {self.tag}, children - [{inner_text[2:]}], props - {self.props})"

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode needs a tag")
        if self.children is None:
            raise ValueError("ParentNode needs children")
        
        inner_html = ""
        for node in self.children:
            inner_html += node.to_html()

        html_string =  f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
        return html_string