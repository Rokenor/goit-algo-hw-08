from bst import NodeBST, insert_bst
from avl import insert_avl

def find_min_value(root: NodeBST):
    '''Знаходить найменше значення в двійковому дереві'''
    if root is None:
        return None
    
    current = root
    # Йдемо до найлівішого вузла
    while current.left is not None:
        current = current.left
    
    return current.key

if __name__ == "__main__":
    # Створення коренів для обох дерев
    root_bst = None
    root_avl = None

    elements = [30, 20, 40, 10, 25, 50, 5]

    # Формування дерев шляхом додавання елементів
    for el in elements:
        root_bst = insert_bst(root_bst, el)
        root_avl = insert_avl(root_avl, el)

    print("Дерева успішно сформовано.")
    print("-" * 30)

    # Пошук найменшого значення в обох деревах
    min_val_bst = find_min_value(root_bst)
    min_val_avl = find_min_value(root_avl)

    print(f"Елементи для вставки: {elements}")
    print(f"Найменше значення в звичайному BST: {min_val_bst}")
    print(f"Найменше значення в AVL-дереві: {min_val_avl}")

    # Перевірка на порожньому дереві
    print("-" * 30)
    min_val_empty = find_min_value(None)
    print(f"Найменше значення в порожньому дереві: {min_val_empty}")