import math
import random
from simple_bandits.algorithms.base_algo import BaseAlgo
from simple_bandits.utils.utils import categorical_draw


class Softmax(BaseAlgo):
    def __init__(self, temperature, counts, values):
        self.temperature = temperature
        self.counts = counts
        self.values = values

    def initialize(self, n_arms: int):
        """## Инициализация

        ### Args:
            - `n_arms (int)`: _description_
        """
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def select_arm(self) -> int:
        """## Выбор руки

        ### Returns:
            - `int`: _description_
        """
        z = sum([math.exp(v / self.temperature) for v in self.values])
        probs = [math.exp(v / self.temperature) / z for v in self.values]
        return categorical_draw(probs)

    def update(self, chosen_arm: int, reward: float):
        """## Обновление бандита

        ### Args:
            - `chosen_arm (int)`: _description_
            - `reward (int)`: _description_
        """
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1
        n = self.counts[chosen_arm]

        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
