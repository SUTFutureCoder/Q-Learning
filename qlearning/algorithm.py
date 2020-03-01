import random
import numpy as np

class Algorithm:
  @staticmethod
  def train(r, q, goals, times, gamma):
    for i in range(times):
      # 随机一个起始点
      state = random.randint(0, len(r) - 1)

      # 单次训练在达到其中一个目标即为完成
      # 当然，这个阈值可以调整为达到多个目标的分数总分
      for goal in goals:
        if state == goal[0]:
          break
        # 存储这个点之后的状态
        next_states = []
        for k, r_next in enumerate(r[state]):
          if r_next != -1:
            next_states.append(k)
        # 对下一个点进行rand
        next_state = next_states[random.randint(0, len(next_states)) - 1]
        q[state][next_state] = r[state][next_state] + gamma * q[next_state].max()
        state = next_state
    return q

  @staticmethod
  def show_path(q, start, goals):
    retstr = str(start)
    current = start
    while True:
      next = np.argmax(q[current])
      for goal in goals:
        if next == goal[0]:
          retstr += " -> " + str(next)
          return retstr
      retstr += " -> " + str(next)
      current = next

