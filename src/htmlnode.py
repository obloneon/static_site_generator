class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # A string representing the HTML tag name.
        self.value = value # A string representing the value of the HTML tag.
        self.children = children # A list of HTMLNode objects representing the children of this node.
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag.

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {str(self.children)}, {str(self.props)})"
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""
        formated_prop_strings = []
        for prop in self.props:
            formated_prop_strings.append( f' {prop}="{self.props[prop]}"')
        return "".join(formated_prop_strings)