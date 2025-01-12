import os
import shutil
from splittext import markdown_to_html_node, extract_title

def copy_source_contents_to_destination(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        raise ValueError(f"Source folder does not exist: {source_folder}")
    
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    
    for content in os.listdir(destination_folder):
        path = os.path.join(destination_folder, content)
        if (os.path.isfile(path)):
            os.remove(path)
        else:
            shutil.rmtree(path)
    
    copy_folder_recursive(source_folder, destination_folder)
    
def copy_folder_recursive(source_folder, destination_folder):
     for content in os.listdir(source_folder):
        source_path = os.path.join(source_folder, content)
        des_path = os.path.join(destination_folder, content)
        
        if (os.path.isfile(source_path)):
            shutil.copy(source_path, des_path)
        else:
            os.mkdir(des_path)
            copy_folder_recursive(source_path, des_path)
            
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as from_file:
        markdown = from_file.read()
    with open(template_path, 'r') as template_file:
        template = template_file.read()
        
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    template = template.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", html)
        
    dest_path_dir = os.path.dirname(dest_path)
    
    if dest_path_dir != "":
        os.makedirs(dest_path_dir, exist_ok=True)
        
    with open(dest_path, 'w') as dest_file:
        dest_file.write(template)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for content in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        if (os.path.isfile(from_path)):
            if (from_path.endswith('.md')):
                generate_page(from_path, template_path, f"{dest_path[:-3]}.html")
        else:
            generate_pages_recursive(from_path, template_path, dest_path)