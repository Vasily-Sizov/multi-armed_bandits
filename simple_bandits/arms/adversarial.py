class AdversarialArm():
    def __init__(self, t: float, active_start: float, active_end: float):
        self.t = t
        self.active_start = active_start
        self.active_end = active_end

    def draw(self) -> float:
        self.t = self.t + 1
        if self.active_start <= self.t <= self.active_end:
            return 1.0
        else:
            return 0.0


if __name__ == "__main__":

    nn = AdversarialArm(t=1, active_start=5, active_end=10)

    for i in range(0, 10):
        value = nn.draw()
        print(value)
