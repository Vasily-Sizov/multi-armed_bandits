import random
from simple_bandits.arms.base_arm import BaseArm


class NormalArm(BaseArm):
    def __init__(self, mu: float, sigma: float):
        self.mu = mu
        self.sigma = sigma

    def draw(self) -> float:
        return random.gauss(self.mu, self.sigma)


if __name__ == "__main__":

    nn = NormalArm(0, 1)
    value = nn.draw()
    print(value)
