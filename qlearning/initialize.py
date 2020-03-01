import numpy as np


class Initialize:
  @staticmethod
  def initRArray(n, path, goals):
    # 初始化
    r_array = np.zeros((n, n), dtype=int)
    r_array[:] = -1
    # 遍历路径，对非goal的进行置0
    for child_path in path:
      # 常规双向设定
      r_array[child_path[0]][child_path[1]] = 0
      r_array[child_path[1]][child_path[0]] = 0

      # 命中目标的情况
      for goal in goals:
        if child_path[1] == goal[0]:
          # 设置为权重
          r_array[child_path[0]][child_path[1]] = goal[1]

    return r_array
