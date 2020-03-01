from qlearning.initialize import Initialize
from qlearning.algorithm import Algorithm
import numpy as np

# 输入格子数量
n = int(input("input n doors\n"))

# 输入可通过路径
print("input path")
path = []
while True:
  path_input = input()
  if path_input == "-1":
    break
  path_input = path_input.split()
  path.append([int(path_input[0]), int(path_input[1])])

print("input goal")
goal = []
while True:
  goal_input = input()
  if goal_input == "-1":
    break
  goal_input = goal_input.split()
  goal.append([int(goal_input[0]), int(goal_input[1])])

# 初始化R矩阵
print("init R array\n")
r_array = Initialize.initRArray(n, path, goal)

# 初始化Q矩阵
print("init Q array\n")
q_array = np.zeros((n, n))

# 输入gamma值
gamma = input("input gamma\n")

# 进行训练
train_times = input("input train times\n")
q = Algorithm.train(r_array, q_array, goal, int(train_times), float(gamma))

# 输出计算后的Q矩阵
print("q array result:\n")
print(q)

# 不断输入一个起始值，输出路径
while True:
  start = input("input the start point number:\n")
  if start == "-1":
    break
  print(Algorithm.show_path(q, int(start), goal))
  print("\n")

