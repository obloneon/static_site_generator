from copy_directory import copy_directory
from generate_page import generate_page

def main():
    copy_directory("static", "public")
    markdown_path = "./content/index.md"
    template_path = "./template.html"
    desination_path = "public/index.html"
    generate_page(markdown_path, template_path, desination_path)

if __name__ == "__main__":
    main()