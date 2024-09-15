import random

from simple_bandits.algorithms.epsilon_greedy.standard import EpsilonGreedy
from simple_bandits.arms.bernoulli import BernoulliArm
from simple_bandits.testing_framework.tests import test_algorithm
from simple_bandits.utils.utils import ind_max


def test_eg_standard(filename: str = 'eg_standard_results.tsv'):
    random.seed(1)
    means = [0.1, 0.1, 0.1, 0.1, 0.9]
    n_arms = len(means)
    random.shuffle(means)
    arms = list(map(lambda mu: BernoulliArm(mu), means))
    print("Best arm is " + str(ind_max(means)))

    f = open(f"{filename}", "w")

    for epsilon in [0.1, 0.2, 0.3, 0.4, 0.5]:
        algo = EpsilonGreedy(epsilon, [], [])
        algo.initialize(n_arms)
        results = test_algorithm(
            algo=algo,
            arms=arms,
            num_sims=5000,
            horizon=250)

        for i in range(len(results[0])):
            f.write(str(epsilon) + "\t")
            f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")

    f.close()
