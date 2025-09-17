class NodeBST:
    '''Клас для представлення вузла двійкового дерева'''
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_bst(root, key):
    '''Рекурсивна функція дл вставки нового ключа в двійкове дерево пошуку'''
    if root is None:
        return NodeBST(key)
    
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
        
    return root