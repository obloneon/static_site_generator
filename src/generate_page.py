import os
from markdown_to_html import markdown_to_html_node, extract_title
from htmlnode import ParentNode

# Takes a md file and transforms it to a HTML file based on a template.
# The result gets saved to the specified desination.
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_content = markdown_to_html_node(markdown).to_html()
    html_title = extract_title(markdown)
    html_file = template.replace("{{ Title }}", html_title)
    html_file = html_file.replace("{{ Content }}", html_content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_file)