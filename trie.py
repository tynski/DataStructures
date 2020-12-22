class TrieNode(object):
    def __init__(self, char):
        self.data = char
        self.children = []

def add_element(root, word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.data == char:
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node       
 
