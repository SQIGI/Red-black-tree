import random

class Dek:
    def __init__(self):
        self._elements = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push_back(self, value: int):
        self._elements.append(value)
        self._size += 1

    def push_front(self, value: int):
        self._elements.insert(0, value)
        self._size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        self._size -= 1
        return self._elements.pop()

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Дек пуст")
        self._size -= 1
        return self._elements.pop(0)

    def reset_program(self):
        self._elements.clear()
        self._size = 0

        with open('/Users/mac/Desktop/Bonch/аопи/851.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        self.push_back(int(line))
                    except ValueError:
                        print(f"Ignoring non-integer value: {line}")

        binary_insertion_sort(self)

        print("Программа была перезагружена. Данные из файла пользователя были загружены и отсортированы.")

def generate_random_numbers_file(filename, num_count):
    with open(filename, 'w') as file:
        for _ in range(num_count):
            random_num = random.randint(-10000, 10000)
            file.write(str(random_num) + '\n')

def choose_file_or_generate_random():
    while True:
        print("\nМеню:")
        print("1. Использовать существующий файл")
        print("2. Создать новый файл с рандомными числами")

        choice = input("Выберите действие: ")

        if choice == '1':
            return '/Users/mac/Desktop/Bonch/аопи/851.txt'
        elif choice == '2':
            num_count = int(input("Введите количество чисел для создания: "))
            new_filename = '/Users/mac/Desktop/Bonch/аопи/new_random_numbers.txt'
            generate_random_numbers_file(new_filename, num_count)
            return new_filename
        else:
            print("Некорректный выбор. Пожалуйста, выберите правильное действие.")

def binary_insertion_sort(dek):
    temp_dek = Dek()

    while not dek.is_empty():
        key = dek.pop_front()

        while not temp_dek.is_empty() and key < temp_dek._elements[-1]:
            dek.push_front(temp_dek.pop_back())

        temp_dek.push_back(key)

    while not temp_dek.is_empty():
        dek.push_back(temp_dek.pop_front())

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = "RED"

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.sorting = []

    def insert(self, key):
        new_node = TreeNode(key)
        if not self.root:
            self.root = new_node
            self.root.color = "BLACK"
        else:
            self._insert_util(self.root, new_node)

    def _insert_util(self, root, new_node):
        if root.key < new_node.key:
            if not root.right:
                root.right = new_node
                new_node.parent = root
            else:
                self._insert_util(root.right, new_node)
        else:
            if not root.left:
                root.left = new_node
                new_node.parent = root
            else:
                self._insert_util(root.left, new_node)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

    def display_tree(self):
        self._display_util(self.root, 0)
        print(self.sorting[::-1])

    def _display_util(self, node, level):
        if node:
            self._display_util(node.right, level + 1)
            self.sorting.append(node.key)
            self._display_util(node.left, level + 1)

def display_sorted_deque(dek):
    print("Отсортированный дек:", dek._elements[:dek._size])
    print("Количество элементов в деке:", dek._size)

def display_unsorted_deque(dek):
    print("Неотсортированный дек:", dek._elements)
    print("Количество элементов в деке:", dek._size)

dek = Dek()
chosen_file = choose_file_or_generate_random()

with open(chosen_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            try:
                dek.push_back(int(line))
            except ValueError:
                print(f"Ignoring non-integer value: {line}")

binary_insertion_sort(dek)

tree = RedBlackTree()
for num in dek._elements:
    tree.insert(num)




while True:
    print("\nМеню:")
    print("1. Показать отсортированный дек и количество элементов")
    print("2. Перейти к использованию файла пользователя")
    print("3. Показать неотсортированный дек и количество элементов")
    print("4. Показать красно-черное дерево с конечным результатом")
    print("5. Выйти из программы")

    choice = input("Выберите действие: ")

    if choice == '1':
        display_sorted_deque(dek)
    elif choice == '2':
        chosen_file = choose_file_or_generate_random()
        dek.reset_program(chosen_file)
    elif choice == '3':
        display_unsorted_deque(dek)
    elif choice == '4':
        tree.display_tree()
    elif choice == '5':
        print("Выход из программы. До свидания!")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите правильное действие.")