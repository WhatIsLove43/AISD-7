import itertools

class Tree:
    def __init__(self, K):
    #Инициализация класса Tree.
    #:param K: количество вершин дерева

        self.K = K  # Количество вершин
        self.edges = []  # Список ребер дерева (для связи между вершинами)
        self.labeling = []  # Оптимальная разметка вершин

    def add_edge(self, parent, child):
    #Добавляет ребро в структуру дерева.
    #:paramparent: родительская вершина
    #:paramchild: дочерняя вершина

        self.edges.append((parent, child))

    def find_leaves(self):
    #Находит листья дерева (вершины, которые не являются родителями).
    #:return: множество листьев

        parents = set(edge[0] for edge in self.edges)
        all_vertices = set(range(1, self.K + 1))
        leaves = all_vertices - parents # Листья — это вершины, которые не в списке родителей
        return leaves

    def find_optimal_labeling(self):
    #Находит оптимальную разметку вершин, максимизирующую сумму чисел на листьях.

        best_sum = float('-inf')  # Переменная для хранения максимальной суммы
        best_labeling = None# Переменная для хранения оптимальной разметки

        # Генерируем все возможные перестановки чисел от 1 до K
        for labeling in itertools.permutations(range(1, self.K + 1)):
            # Сопоставляем метки вершинам
            vertex_labels = {i + 1: labeling[i] for i in range(self.K)}
            leaves = self.find_leaves()  # Находим листья текущего дерева
            leaf_sum = sum(vertex_labels[leaf] for leaf in leaves)  # Суммируем метки на листьях

            # Обновляем оптимальную разметку, если текущая лучше
            if leaf_sum>best_sum:
                best_sum = leaf_sum
                best_labeling = vertex_labels

        # Сохраняем оптимальную разметку
        self.labeling = best_labeling
        print("Оптимальная разметка вершин:")
        for vertex, label in self.labeling.items():
            print(f"Вершина{vertex}: {label}")
        print(f"Максимальная сумма чисел на листьях: {best_sum}")


def main():
    # Ввод данных
    K = int(input("Введите количество вершин дерева (K): "))
    tree = Tree(K)

    print("Введите ребра дерева в формате 'родитель дочерний' (для завершения введите пустую строку):")
    while True:
        edge = input()
        if not edge:  # Если строка пустая, завершаем ввод
            break
        parent, child = map(int, edge.split())
        tree.add_edge(parent, child)

    # Вывод структуры дерева
    print("\nСтруктура дерева (ребра):")
    for edge in tree.edges:
        print(f"{edge[0]} ->{edge[1]}")

    # Нахождение оптимальной разметки
    tree.find_optimal_labeling()


if __name__ == "__main__":
    main()
