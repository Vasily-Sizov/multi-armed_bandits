import math
import random
from algorithms.base_algo import BaseAlgo


class Hedge(BaseAlgo):
    def __init__(self, temperature, counts, values):
        self.temperature = temperature
        self.counts = counts
        self.values = values

    @staticmethod
    def categorical_draw(probs):
        z = random.random()
        cum_prob = 0.0
        for i in range(len(probs)):
            prob = probs[i]
            cum_prob += prob
            if cum_prob > z:
                return i

        return len(probs) - 1

    def initialize(self, n_arms: int) -> None:
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
        return Hedge.categorical_draw(probs)

    def update(self, chosen_arm: int, reward: int) -> None:
        """## Обновление бандита

        ### Args:
            - `chosen_arm (int)`: _description_
            - `reward (int)`: _description_
        """
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1

        value = self.values[chosen_arm]
        self.values[chosen_arm] = value + reward
