# Simulated Annealing
import random

from graph import *


def rand_swap(ls: list):
    n = len(ls)
    x, y = divmod(random.randint(0, n * (n - 1)), n)
    if x == y:
        x = n - 1
    ls[x], ls[y] = ls[y], ls[x]


if __name__ == '__main__':
    graph = get_graph()
    alpha = 0.99
    t_lowest = 0.01
    limit_iteration = 1000
    limit_unchanged = 150

    t_cur = 150
    path_best = path_cur = list(range(14))
    dist_best = dist_cur = graph.cal_path_dist(path_cur)

    while t_cur > t_lowest:
        count_unchanged = 0
        count_iteration = 0
        while count_unchanged < limit_unchanged and count_iteration < limit_iteration:
            path_new = path_cur.copy()
            rand_swap(path_new)
            dist_new = graph.cal_path_dist(path_new)
            dist_delta = dist_new - dist_cur
            if dist_delta < 0 or math.exp(-dist_delta / t_cur) > random.random():
                path_cur = path_new
                dist_cur = dist_new
                if dist_cur < dist_best:
                    dist_best = dist_cur
                    path_best = path_cur
            else:
                count_unchanged += 1
            count_iteration += 1
        t_cur *= alpha

    print(f"环路: {'->'.join(map(lambda x: str(x + 1), path_best))}")
    print(f"花费时间: {dist_best / 20}h")
