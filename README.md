# Q-Learning  
用于复现北航AI智能无人系统第一讲增强学习算法  

http://mnemstudio.org/path-finding-q-learning-tutorial.htm  

**了解原理，动手编程，反复实验，实际应用** 

# 解决问题


# INPUT & OUTPUT  
```
input n doors
8
input path
0 4 
4 5
5 1
5 6
1 2
6 2
6 7
2 3
-1
input goal
3 100
-1
init R array

init Q array

input gamma
0.8
input train times
10000
q array result:

[[  0.      0.      0.      0.     40.96    0.      0.      0.   ]
 [  0.      0.     80.      0.      0.     51.2     0.      0.   ]
 [  0.     64.      0.    100.      0.      0.     64.      0.   ]
 [  0.      0.      0.      0.      0.      0.      0.      0.   ]
 [ 32.768   0.      0.      0.      0.     51.2     0.      0.   ]
 [  0.     64.      0.      0.     40.96    0.     64.      0.   ]
 [  0.      0.     80.      0.      0.     51.2     0.     51.2  ]
 [  0.      0.      0.      0.      0.      0.     64.      0.   ]]


input the start point number:
0
0 -> 4 -> 5 -> 1 -> 2 -> 3


input the start point number:
1
1 -> 2 -> 3


input the start point number:
2
2 -> 3


input the start point number:
3
3 -> 0 -> 4 -> 5 -> 1 -> 2 -> 3


input the start point number:
4
4 -> 5 -> 1 -> 2 -> 3


input the start point number:
5
5 -> 1 -> 2 -> 3


input the start point number:
6
6 -> 2 -> 3


input the start point number:
7
7 -> 6 -> 2 -> 3


input the start point number:
-1

```