import itertools

class Tree:
    def init(self, K):
        self.K = K
        self.vertices = list(range(1, K + 1))
        self.leaf_indices = self.get_leaf_indices()

    def is_even(self, n):
        return n % 2 == 0

    def get_leaf_indices(self):
        if self.K % 2 == 0:
            return list(range((self.K // 2), self.K))
        else:
            return list(range(((self.K // 2) + 1), self.K))

    def find_optimal_labeling(self):
        if self.K <= 0:
            print("Количество вершин должно быть положительным числом.")
            return

        optimal_labeling = None
        min_leaf_sum = float('inf')

        for labeling in itertools.permutations(self.vertices):
            leaf_values = [labeling[i] for i in self.leaf_indices]

            if all(self.is_even(value) for value in leaf_values):
                leaf_sum = sum(leaf_values)
                if leaf_sum < min_leaf_sum:
                    min_leaf_sum = leaf_sum
                    optimal_labeling = labeling

        if optimal_labeling:
            print(f"Оптимальная разметка: {optimal_labeling}")
            print(f"Минимальная сумма чисел на листьях: {min_leaf_sum}")
        else:
            print("Не найдено разметок, удовлетворяющих условиям.")

K = int(input("Введите количество вершин K: "))
tree_labeling = Tree(K)
tree_labeling.find_optimal_labeling()
