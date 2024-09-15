from abc import ABC, abstractmethod


class BaseArm(ABC):

    @abstractmethod
    def draw(self) -> float:
        pass
