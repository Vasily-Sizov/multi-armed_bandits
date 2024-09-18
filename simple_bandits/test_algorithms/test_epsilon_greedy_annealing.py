import random

from simple_bandits.algorithms.epsilon_greedy.annealing import AnnealingEpsilonGreedy
from simple_bandits.arms.bernoulli import BernoulliArm
from simple_bandits.testing_framework.tests import test_algorithm
from simple_bandits.utils.utils import ind_max


def test_eg_annealing(filename: str = 'eg_annealing_results.tsv',):
    random.seed(1)
    means = [0.1, 0.1, 0.1, 0.1, 0.9]
    n_arms = len(means)
    random.shuffle(means)
    arms = list(map(lambda mu: BernoulliArm(mu), means))
    print("Best arm is " + str(ind_max(means)))

    algo = AnnealingEpsilonGreedy([], [])
    algo.initialize(n_arms)

    results = test_algorithm(
        algo=algo,
        arms=arms,
        num_sims=5000,
        horizon=250)

    f = open(f"{filename}", "w")

    for i in range(len(results[0])):
        f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")

    f.close()
