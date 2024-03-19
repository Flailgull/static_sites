class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        
        result = ""
        for key in self.props:
            result += " " + key + "=\"" + self.props[key] + "\""
        return result
    
    def __repr__(self) -> str:
        return f"HTMLNode(tag - {self.tag}, value - {self.value}, children - {self.children}, props - {self.props})"