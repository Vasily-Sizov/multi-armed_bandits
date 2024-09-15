import random
from arms.base_arm import BaseArm


class BernoulliArm(BaseArm):
    def __init__(self, p: float):
        self.p = p

    def draw(self) -> float:
        if random.random() > self.p:
            return 0.0
        else:
            return 1.0


if __name__ == "__main__":

    nn = BernoulliArm(0.3)
    value = nn.draw()
    print(value)
