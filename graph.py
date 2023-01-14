import math


class Graph:
    def __init__(self, paths: list[list], n: int):
        """
        Floyd 算法求各点之间的最短路
        :param paths: 路径，格式: [端点A,端点B,距离]
        :param n: 点的数量
        """
        self.dists = [[math.inf] * n for _ in range(n)]
        for x, y, l in paths:
            self.dists[x - 1][y - 1] = l
            self.dists[y - 1][x - 1] = l
        for i in range(n):
            self.dists[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.dists[j][i] = self.dists[i][j] = min(self.dists[i][j], self.dists[i][k] + self.dists[k][j])

    def cal_path_dist(self, path: list[int]):
        """
        计算环路的长度
        """
        return self.dists[path[0]][path[-1]] + sum(self.dists[path[i]][path[i + 1]] for i in range(len(path) - 1))


def get_graph() -> Graph:
    return Graph([
        [1, 5, 540],
        [1, 7, 550],
        [1, 11, 260],
        [2, 3, 560],
        [2, 5, 180],
        [3, 5, 440],
        [4, 6, 280],
        [5, 6, 510],
        [5, 7, 340],
        [5, 8, 560],
        [5, 9, 480],
        [6, 9, 270],
        [6, 10, 420],
        [7, 8, 360],
        [7, 12, 380],
        [8, 9, 290],
        [8, 12, 330],
        [9, 10, 610],
        [9, 12, 290],
        [9, 13, 420],
        [9, 14, 360],
        [10, 14, 250],
        [11, 12, 240],
        [13, 14, 470]
    ], 14)
