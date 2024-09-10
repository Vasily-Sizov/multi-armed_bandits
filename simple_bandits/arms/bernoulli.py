import random


class BernoulliArm:
    def __init__(self, p: float):
        self.p = p

    def draw(self) -> float:
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0
