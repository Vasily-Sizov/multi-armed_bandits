import math
from algorithms.base_algo import BaseAlgo


def ind_max(x):
    m = max(x)
    return x.index(m)


class UCB1(BaseAlgo):
    def __init__(self, counts, values) -> None:
        self.counts = counts
        self.values = values

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
        n_arms = len(self.counts)
        for arm in range(n_arms):
            if self.counts[arm] == 0:
                return arm

        ucb_values = [0.0 for arm in range(n_arms)]
        total_counts = sum(self.counts)
        for arm in range(n_arms):
            bonus = math.sqrt((2 * math.log(total_counts)) / float(self.counts[arm]))
            ucb_values[arm] = self.values[arm] + bonus
        return ind_max(ucb_values)

    def update(self, chosen_arm: int, reward: int) -> None:
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
