import random


class EpsilonGreedy:
    """## Эпсилон-жадный алгоритм"""

    def __init__(self, epsilon: float, counts: list, values: list):
        """## Конструктор

        ### Args:
            - `epsilon (float)`: Коэффициент исследования
            - `counts (list)`: Вектор сколько раз сыграли каждой из рук
            - `values (list)`: Вектор с вознаграждениями
        """
        self.epsilon = epsilon
        self.counts = counts
        self.values = values

    @staticmethod
    def ind_max(x: list):
        m = max(x)
        return x.index(m)

    def initialize(self, n_arms: int) -> None:
        """## Инифиализация

        ### Args:
            - `n_arms (int)`: Количество рук
        """
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def select_arm(self) -> int:
        """## Выбор руки

        ### Returns:
            - `int`: рука
        """
        if random.random() > self.epsilon:
            return EpsilonGreedy.ind_max(self.values)
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


if __name__ == "__main__":

    # Случайное поведение
    algo = EpsilonGreedy(epsilon=1.0, counts=[], values=[])
    algo.initialize(n_arms=2)

    # Максимизация прибыли
    algo = EpsilonGreedy(epsilon=0.0, counts=[], values=[])
    algo.initialize(n_arms=2)
