import random
import math
from simple_bandits.algorithms.base_algo import BaseAlgo
from simple_bandits.utils.utils import categorical_draw


class Exp3(BaseAlgo):
    def __init__(self, gamma, weights):
        self.gamma = gamma
        self.weights = weights

    def initialize(self, n_arms: int) -> None:
        """## Инициализация

        ### Args:
            - `n_arms (int)`: Количество рук
        """
        self.weights = [1.0 for i in range(n_arms)]

    def select_arm(self) -> int:
        """## Выбор руки

        ### Returns:
            - `int`: Возвращает руку
        """
        n_arms = len(self.weights)
        total_weight = sum(self.weights)
        probs = [0.0 for i in range(n_arms)]
        for arm in range(n_arms):
            probs[arm] = (1 - self.gamma) * (self.weights[arm] / total_weight)
            probs[arm] = probs[arm] + (self.gamma) * (1.0 / float(n_arms))
        return categorical_draw(probs)

    def update(self, chosen_arm: int, reward: float) -> None:
        """## Обновление бандита

        ### Args:
            - `chosen_arm (int)`: _description_
            - `reward (int)`: _description_
        """
        n_arms = len(self.weights)
        total_weight = sum(self.weights)
        probs = [0.0 for i in range(n_arms)]
        for arm in range(n_arms):
            probs[arm] = (1 - self.gamma) * (self.weights[arm] / total_weight)
            probs[arm] = probs[arm] + (self.gamma) * (1.0 / float(n_arms))

        x = reward / probs[chosen_arm]

        growth_factor = math.exp((self.gamma / n_arms) * x)
        self.weights[chosen_arm] = self.weights[chosen_arm] * growth_factor
