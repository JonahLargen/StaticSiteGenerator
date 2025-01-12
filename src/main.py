from contents import copy_source_contents_to_destination, generate_page

def main():
    copy_source_contents_to_destination("static", "public")
    generate_page('content/index.md', 'template.html', 'public/index.html')
        
main()