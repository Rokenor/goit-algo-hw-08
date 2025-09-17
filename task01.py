class Node:
    '''Клас для представлення вузла двійкового дерева'''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def insert_bst(root, key):
    '''Рекурсивна функція дл вставки нового ключа в двійкове дерево пошуку'''
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
        
    return root

def find_min_value(root: Node):
    '''Знаходить найменше значення в двійковому дереві'''
    if root is None:
        return None
    
    current = root
    # Йдемо до найлівішого вузла
    while current.left is not None:
        current = current.left
    
    return current.key

if __name__ == "__main__":
    # Створення кореня для дерева
    root_bst = None

    elements = [30, 20, 40, 10, 25, 50, 5]

    # Формування дерева шляхом додавання елементів
    for el in elements:
        root_bst = insert_bst(root_bst, el)

    print("Дерево успішно сформовано.")
    print("-" * 30)

    # Пошук найменшого значення в дереві
    min_val_bst = find_min_value(root_bst)

    print(f"Елементи для вставки: {elements}")
    print(f"Найменше значення в BST: {min_val_bst}") 

    # Перевірка на порожньому дереві
    print("-" * 30)
    min_val_empty = find_min_value(None)
    print(f"Найменше значення в порожньому дереві: {min_val_empty}")