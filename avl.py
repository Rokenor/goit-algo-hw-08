class NodeAVL:
    '''Клас для представлення вузла AVL-дерева'''
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    '''Допоміжна функція для отримання висоти вузла'''
    if not node:
        return 0
    return node.height

def get_balance(node):
    '''Допоміжна функція для отримання фактора балансу вузла'''
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(z):
    '''Функція для правого повороту піддерева з коренем z'''
    y = z.left
    T3 = y.right

    # Виконання повороту
    y.right = z
    z.left = T3

    # Оновлення висот
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def left_rotate(z):
    '''Функція для лівого повороту піддерева з коренем z'''
    y = z.right
    T2 = y.left

    # Виконання повороту
    y.left = z
    z.right = T2

    # Оновлення висот
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def insert_avl(root, key):
    '''Рекурсивна функція для вставки ключа в AVL-дерево з подальшим балансуванням'''
    # Стандартна вставка BST
    if not root:
        return NodeAVL(key)
    elif key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    # Оновлення висоти поточного вузла
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Отримання фактора балансу
    balance = get_balance(root)

    # Якщо вузол розбалансований, виконуємо один з 4-х випадків балансування

    # Випадок 1: Left Left (LL)
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Випадок 2: Right Right (RR)
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Випадок 3: Left Right (LR)
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Випадок 4: Right Left (RL)
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
