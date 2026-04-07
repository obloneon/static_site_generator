from copy_directory import copy_directory
from generate_page import generate_pages_recursive

def main():
    copy_directory("static", "public")
    content_path = "./content"
    template_path = "./template.html"
    destination_path = "./public"
    generate_pages_recursive(content_path, template_path, destination_path)

if __name__ == "__main__":
    main()