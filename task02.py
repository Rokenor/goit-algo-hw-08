from bst import insert_bst
from avl import insert_avl

def sum_tree_values(root):
    '''Рекурсивно обчислює суму всіх значень в двійковому дереві'''
    if not root:
        return 0
    
    return root.key + sum_tree_values(root.left) + sum_tree_values(root.right)

if __name__ == "__main__":
    # Створимо набір даних для вставки
    keys = [10, 20, 30, 40, 50, 25]

    # Робота з двійковим деревом пошуку (BST)
    root_bst = None
    for key in keys:
        root_bst = insert_bst(root_bst, key)
    
    sum_bst = sum_tree_values(root_bst)
    print(f"Двійкове дерево пошуку (BST):")
    print(f"Сума всіх значень: {sum_bst}")
    
    print("-" * 20)

    # Робота з AVL-деревом
    root_avl = None
    for key in keys:
        root_avl = insert_avl(root_avl, key)
        
    sum_avl = sum_tree_values(root_avl)
    print(f"AVL-дерево:")
    print(f"Сума всіх значень: {sum_avl}")
    
    print("-" * 20)

    # Перевіримо правильність розрахунку
    expected_sum = sum(keys)
    print("-" * 20)
    print(f"Очікувана сума (для перевірки): {expected_sum}")