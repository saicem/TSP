# Tabu Search
import random
from collections import deque

from graph import *

if __name__ == '__main__':
    graph = get_graph()
    tabu_table_len = 30

    path_cur = list(range(14))
    random.shuffle(path_cur)
    dist_cur = graph.cal_path_dist(path_cur)
    paths = [path_cur]
    dists = [dist_cur]
    tabu_table = deque([path_cur])

    def find_new_paths(path: list):
        ret = []
        n = len(path)
        for i in range(n - 1):
            for j in range(i + 1, n):
                path_new = path.copy()
                path_new[i], path_new[j] = path_new[j], path_new[i]
                if path_new not in tabu_table:
                    ret.append(path_new)
        return ret


    for _ in range(10000):
        paths_new = find_new_paths(path_cur)
        dists_new = list(map(graph.cal_path_dist, paths_new))
        dist_best = min(dists_new)
        path_best = paths_new[dists_new.index(dist_best)]
        if dist_best < dist_cur:
            dist_cur = dist_best
            path_cur = path_best
        tabu_table.append(path_best)
        if len(tabu_table) > tabu_table_len:
            tabu_table.popleft()

    print(f"环路: {'->'.join(map(lambda x: str(x + 1), path_cur))}")
    print(f"花费时间: {dist_cur / 20}h")
