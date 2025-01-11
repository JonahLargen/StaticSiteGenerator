import os
import shutil

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