import sys

from copy_directory import copy_directory
from generate_page import generate_pages_recursive

def main():
    copy_directory("static", "docs")
    base_path = sys.argv[1]
    if base_path == "":
        base_path = "/"
    content_path = "./content"
    template_path = "./template.html"
    destination_path = "./docs"
    generate_pages_recursive(base_path, content_path, template_path, destination_path)

if __name__ == "__main__":
    main()