from abc import ABC, abstractmethod


class BaseAlgo(ABC):

    @abstractmethod
    def initialize(self, n_arms: int) -> None:
        pass

    @abstractmethod
    def select_arm(self) -> int:
        pass

    @abstractmethod
    def update(self, chosen_arm: int, reward: int) -> None:
        pass
