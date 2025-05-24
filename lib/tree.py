class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Handle empty tree case
        if self.root is None:
            return None
            
        # Use a stack for DFS (pre-order traversal)
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            # Check if current node matches the ID
            if node.get('id') == id:
                return node
            # Add children to stack in reverse order to process left-to-right
            stack.extend(reversed(node.get('children', [])))
        
        # Return None if no matching node found
        return None