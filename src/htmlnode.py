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


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {str(self.props)})"
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("object of type ParentNode has no tag")
        if self.children == None:
            raise ValueError("object of type ParentNode has no children")
        children_result = []
        for child in self.children:
            children_result.append(child.to_html())
        return f"<{self.tag}{self.props_to_html()}>{"".join(children_result)}</{self.tag}>"