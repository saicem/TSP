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
    path_best_1 = path_cur_1 = list(range(7))
    path_best_2 = path_cur_2 = list(range(7, 14))
    dist_best = dist_cur = max(graph.cal_path_dist(path_cur_1), graph.cal_path_dist(path_cur_2))
    while t_cur > t_lowest:
        count_unchanged = 0
        count_iteration = 0
        while count_unchanged < limit_unchanged and count_iteration < limit_iteration:
            path_1_new = path_cur_1.copy()
            path_2_new = path_cur_2.copy()
            action = random.randint(1, 4)
            if action == 1:
                rand_swap(path_1_new)
            if action == 2:
                rand_swap(path_2_new)
            if action == 3:
                i = random.randint(0, len(path_1_new) - 1)
                j = random.randint(0, len(path_2_new) - 1)
                path_1_new[i], path_2_new[j] = path_2_new[j], path_1_new[i]
            if action == 4:
                i = random.randint(0, len(path_1_new) - 1)
                j = random.randint(0, len(path_2_new) - 1)
                if len(path_2_new) == 1 or random.random() > 0.5 and len(path_1_new) != 1:
                    path_2_new.insert(j, path_1_new.pop(i))
                else:
                    path_1_new.insert(i, path_2_new.pop(j))

            dist_new = max(graph.cal_path_dist(path_1_new), graph.cal_path_dist(path_2_new))
            dist_delta = dist_new - dist_cur
            if dist_delta < 0 or math.exp(-dist_delta / t_cur) > random.random():
                path_cur_1 = path_1_new
                path_cur_2 = path_2_new
                dist_cur = dist_new
                if dist_cur < dist_best:
                    dist_best = dist_cur
                    path_best_1 = path_cur_1
                    path_best_2 = path_cur_2
            else:
                count_unchanged += 1
            count_iteration += 1
        t_cur *= alpha

    print(f"环路1: {'->'.join(map(lambda x: str(x + 1), path_best_1))}")
    print(f"环路2: {'->'.join(map(lambda x: str(x + 1), path_best_2))}")
    print(f"花费时间: {dist_best / 20}h")
