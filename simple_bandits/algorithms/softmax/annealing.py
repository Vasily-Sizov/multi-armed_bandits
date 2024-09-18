import math
from simple_bandits.algorithms.base_algo import BaseAlgo
from simple_bandits.utils.utils import categorical_draw


class AnnealingSoftmax(BaseAlgo):
    """## Softmax алгоритм с отжигом"""

    def __init__(self, counts: list[int], values: list[float]):
        """## Конструктор

        ### Args:
            - `counts (list[int])`: Вектор - сколько раз сыграли каждой из рук
            - `values (list[float])`: Вектор с вознаграждениями
        """
        self.counts = counts
        self.values = values

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
            - `int`: Возвращает руку
        """
        t = sum(self.counts) + 1
        temperature = 1 / math.log(t + 0.0000001)

        z = sum([math.exp(v / temperature) for v in self.values])
        probs = [math.exp(v / temperature) / z for v in self.values]
        return categorical_draw(probs)

    def update(self, chosen_arm: int, reward: float) -> None:
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
