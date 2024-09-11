import random
import math


class AnnealingEpsilonGreedy():
    """## Эпсилон-жадный алгоритм с отжигом"""

    def __init__(self, counts: list, values: list):
        """## Конструктор

        ### Args:
            - `counts (_type_)`: Вектор - сколько раз сыграли каждой из рук
            - `values (_type_)`: Вектор с вознаграждениями
        """
        self.counts = counts
        self.values = values

    @staticmethod
    def ind_max(x: list) -> int:
        m = max(x)
        return x.index(m)

    def initialize(self, n_arms: int) -> None:
        """## Инициализация

        ### Args:
            - `n_arms (int)`: Количество рук
        """
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def select_arm(self) -> int:
        """## Выбор руки

        ### Returns:
            - `_type_`: Возвращает руку
        """
        t = sum(self.counts) + 1
        epsilon = 1 / math.log(t + 0.0000001)

        if random.random() > epsilon:
            return AnnealingEpsilonGreedy.ind_max(self.values)
        else:
            return random.randrange(len(self.values))

    def update(self, chosen_arm: int, reward: int) -> None:
        """## Обновление бандита

        ### Args:
            - `chosen_arm (int)`: Выбранная рука
            - `reward (int)`: Награда
        """
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1
        n = self.counts[chosen_arm]

        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
