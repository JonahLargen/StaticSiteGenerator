from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if (old_node.text_type != TextType.TEXT):
            new_nodes.append(old_node)
            continue
        
        sections = old_node.text.split(delimiter)
        
        if (len(sections) %2 == 0):
            raise ValueError("Invalid markdown syntax, all markdown that is opened must be closed by a matching tag")
        
        text_field = True
        
        for section in sections:
            if (section == ""):
                continue
            
            if (text_field):
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))
                
            text_field = not text_field

    return new_nodes