class TreeType:
    """Клас для збереження загальних даних про тип дерева (легковаговик)"""
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Малювання {self.name} кольорове дерево {self.color} в ({x}, {y})")

class TreeFactory:
    """Фабрика для створення або повторного використання об'єктів TreeType"""
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        if (name, color, texture) not in TreeFactory._tree_types:
            TreeFactory._tree_types[(name, color, texture)] = TreeType(name, color, texture)
        return TreeFactory._tree_types[(name, color, texture)]

class Tree:
    """Клас, що представляє дерево з унікальним зовнішнім станом"""
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)

class Forest:
    """Клас для створення дерев з використанням легковаговиків"""
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw_forest(self):
        for tree in self.trees:
            tree.draw()

# Використання
forest = Forest()
forest.plant_tree(10, 20, "Дуб", "Зелений", "Гладкий")
forest.plant_tree(15, 25, "Сосна", "Темно-зелений", "Грубий")
forest.plant_tree(10, 20, "Дуб", "Зелений", "Гладкий")  # Використовує вже існуючий легковаговик
forest.draw_forest()
