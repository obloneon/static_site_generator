import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_html(self):
        node = HTMLNode()
        test_string = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), test_string)
    
    def test_repr_html2(self):
        node = HTMLNode(tag="<p>", value="text", children=[HTMLNode()], props={"target": "_blank"} )
        test_string = "HTMLNode(<p>, text, [HTMLNode(None, None, None, None)], {'target': '_blank'})"
        self.assertEqual(repr(node), test_string)
    
    def test_repr_leaf(self):
        node = LeafNode(tag="<p>", value="text", props={"target": "_blank"})
        test_string = "LeafNode(<p>, text, {'target': '_blank'})"
        self.assertEqual(repr(node), test_string)
   
    def test_props_to_html(self):
        node = HTMLNode()
        test_string = ""
        self.assertEqual(node.props_to_html(), test_string)
    
    def test_props_to_html2(self):
        node = HTMLNode(props={})
        test_string = ""
        self.assertEqual(node.props_to_html(), test_string)
    
    def test_props_to_html3(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
                }
            )
        test_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), test_string)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="just text")
        self.assertEqual(node.to_html(), "just text")

    def test_to_html_value_none(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    def test_parentnode_no_tag_raises(self):
        child = LeafNode("span", "child")
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[child]).to_html()

    def test_parentnode_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=None).to_html()


if __name__ == "__main__":
    unittest.main()