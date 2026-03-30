import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode()
        test_string = "HTMLNode(None, None, None, None)"
        self.assertEqual(repr(node), test_string)
    def test_repr2(self):
        node = HTMLNode(tag="<p>", value="text", children=[HTMLNode()], props={"target": "_blank"} )
        test_string = "HTMLNode(<p>, text, [HTMLNode(None, None, None, None)], {'target': '_blank'})"
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

if __name__ == "__main__":
    unittest.main()