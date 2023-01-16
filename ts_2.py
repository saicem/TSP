# Tabu Search
import itertools
import random
from collections import deque

from graph import *

if __name__ == '__main__':
    graph = get_graph()
    tabu_table_len = 300


    def eval_dist(path_1: list, path_2: list):
        return max(graph.cal_path_dist(path_1), graph.cal_path_dist(path_2))

    def hash_path(path_1: list, path_2: list):
        return hash(str(path_1) + '.' + str(path_2))

    path_best_1 = path_cur_1 = list(range(7))
    path_best_2 = path_cur_2 = list(range(7, 14))
    random.shuffle(path_cur_1)
    random.shuffle(path_cur_2)
    dist_best = dist_cur = eval_dist(path_cur_1, path_cur_2)
    hashed_path = hash_path(path_cur_1, path_cur_2)
    tabu_deque = deque([hashed_path])
    tabu_table = {hashed_path}


    def swap_paths(path: list):
        n = len(path)
        for i in range(n - 1):
            for j in range(i + 1, n):
                path_new = path.copy()
                path_new[i], path_new[j] = path_new[j], path_new[i]
                yield path_new


    def exchange_paths(path_1: list, path_2: list):
        l1, l2 = len(path_1), len(path_2)
        for i in range(l1):
            for j in range(l2):
                p1, p2 = path_1.copy(), path_2.copy()
                p1[i], p2[j] = p2[j], p1[i]
                yield p1, p2
                if l1 > 1:
                    p1, p2 = path_1.copy(), path_2.copy()
                    p2.insert(j, p1.pop(i))
                    yield p1, p2
                if l2 > 1:
                    p1, p2 = path_1.copy(), path_2.copy()
                    p1.insert(i, p2.pop(j))
                    yield p1, p2


    for _ in range(10000):
        dist_nex = math.inf
        path_nex_1 = None
        path_nex_2 = None
        for p1, p2 in itertools.chain([(x, path_cur_2) for x in swap_paths(path_cur_1)],
                                      [(path_cur_1, x) for x in swap_paths(path_cur_2)],
                                      exchange_paths(path_cur_1, path_cur_2)):
            hashed_path = hash_path(p1, p2)
            if hashed_path in tabu_table:
                continue
            dist_new = eval_dist(p1, p2)
            if dist_new < dist_nex:
                dist_nex = dist_new
                path_nex_1 = p1
                path_nex_2 = p2
                tabu_table.add(hashed_path)
                tabu_deque.append(hashed_path)
                if len(tabu_table) > tabu_table_len:
                    tabu_table.remove(tabu_deque.popleft())

        dist_cur = dist_nex
        path_cur_1 = path_nex_1
        path_cur_2 = path_nex_2
        if dist_cur < dist_best:
            dist_best = dist_cur
            path_best_1 = path_cur_1
            path_best_2 = path_cur_2

    print(f"环路1: {'->'.join(map(lambda x: str(x + 1), path_best_1))}")
    print(f"环路2: {'->'.join(map(lambda x: str(x + 1), path_best_2))}")
    print(f"花费时间: {dist_best / 20}h")
