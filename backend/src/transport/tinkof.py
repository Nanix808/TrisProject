# import datetime
# print(datetime.datetime.now())

# Задача 6

# Ну и конечно же задача на блуждания коня по шахматной доске размера ﻿
# �
# ×
# �
# n×n﻿. Чтобы блуждать не было скучно, на доске разбросаны специальные фишки.

# Есть два типа фишек — "﻿
# �
# K﻿" и "﻿
# �
# G﻿". При ходе в клетку, в которой лежит фишка "﻿
# �
# K﻿", фигура превращается в коня. При ходе в клетку, в которой лежит фишка "﻿
# �
# G﻿", фигура превращается в короля. Разумеется, после превращения фигура начинает ходить соответственно своему новому типу. Попадание короля в клетку с фишкой "﻿
# �
# G﻿" или коня в клетку с фишкой "﻿
# �
# K﻿" ничего не меняет. При этом трансформация является обязательной и фигура не может пройти такую клетку с фишкой без превращения в указанный тип.

# Ваша задача определить, за какое минимальное количество ходов фигура (возможно в образе коня/короля) доберется до заданной клетки. Заметьте, что количество трансформаций считать не нужно.

# Формат входных данных

# В первой строке задано одно натуральное число ﻿
# �
# n﻿ — размер доски ﻿
# (
# 2
# ≤
# �
# ≤
# 100
# )
# (2≤n≤100)﻿. В следующих ﻿
# �
# n﻿ клетках задано описание шахматной доски — по ﻿
# �
# n﻿ символов. Фишки обозначаются "﻿
# �
# K﻿" и "﻿
# �
# G﻿", а пустые клетки за "﻿
# .
# .﻿". Начальная клетка обозначается "﻿
# �
# S﻿", а конечная — "﻿
# �
# F﻿".

# Гарантируется, что на начальной и конечной клетках нет фишки.

# Формат выходных данных

# Выведите единственное число — необходимое количество ходов. Если такого пути не существует, то выведите ﻿
# −
# 1
# −1﻿.

# Замечание

# Как и всегда, конь ходит буквой ﻿
# Г
# Г﻿, т.е. на одну клетку в одну сторону и две клетки в другую, всего до ﻿
# 8
# 8﻿ возможных ходов. Король может перейти из текущей клетки в соседнюю по стороне или углу, всего до ﻿
# 8
# 8﻿ возможных ходов.


# from collections import deque


# def min_moves(board, n):
#     n = len(board)

#     # Список смещений для возможных ходов коня и короля
#     knight_moves = [
#         (2, 1),
#         (1, 2),
#         (-1, 2),
#         (-2, 1),
#         (-2, -1),
#         (-1, -2),
#         (1, -2),
#         (2, -1),
#     ]
#     king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

#     # Находим начальную позицию "S" и целевую позицию "F"
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == "S":
#                 start = (i, j, "N")  # Начинаем с коня
#             elif board[i][j] == "F":
#                 target = (i, j)

#     # Начальная позиция и шаги
#     queue = deque([(start, 0)])

#     # Помеченные клетки
#     marked = set()
#     marked.add(start)

#     # Пока очередь не пуста
#     while queue:
#         (x, y, piece), steps = queue.popleft()

#         # Если достигли цели, вернуть количество шагов
#         if (x, y) == target:
#             return steps

#         # Выбираем список ходов в зависимости от типа фигуры
#         moves = knight_moves if piece == "N" else king_moves

#         # Проверяем все возможные ходы из текущей клетки
#         for dx, dy in moves:
#             nx, ny = x + dx, y + dy

#             # Если клетка находится в пределах доски
#             if 0 <= nx < n and 0 <= ny < n:
#                 # Если клетка не занята препятствием
#                 if board[nx][ny] != "#":
#                     new_piece = piece
#                     # Если в клетке есть фишка, изменяем тип фигуры
#                     if board[nx][ny] == "K":
#                         new_piece = "N"
#                     elif board[nx][ny] == "G":
#                         new_piece = "K"
#                     new_pos = (nx, ny, new_piece)
#                     # Если новая позиция не помечена, добавляем ее в очередь и помечаем
#                     if new_pos not in marked:
#                         marked.add(new_pos)
#                         queue.append((new_pos, steps + 1))
#     return -1


# n = int(input())
# board = [list(input().strip()) for _ in range(n)]
# print(min_moves(board, n))


# Задание 1
# def main():
# n = int(input())
# assessment_per_days = [int(x) for x in input().split()]
# interval = 7
# max_assessment = -1
# for i in range(n - interval + 1):
#     assessment_per_interval = assessment_per_days[i:interval + i]
#     if 2 in assessment_per_interval or 3 in assessment_per_interval:
#         continue
#     else:
#         count = assessment_per_interval.count(5)
#         if count > max_assessment:
#             max_assessment = count
# print(max_assessment)

# задание 2
# def main():

#     n, m = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(n)]

#     matrix.reverse()
#     for i in range(m):
#         for j in range(n):
#             print(matrix[j][i], end=" ")
#         print()

# Задание 3
# def main():
#     n = int(input())
#     directory = [input() for _ in range(n)]
#     dir_dict = {}
#     for dir in directory:
#         dir_list = dir.split("/")
#         for i in range(len(dir_list)):
#             dir_dict["/".join(dir_list[: i + 1])] = i
#     sorted_dirs = sorted(dir_dict.items(), key=lambda x: x[0])
#     for dir, level in sorted_dirs:
#         print("  " * level + dir.split("/")[-1])

# задание 4
# def main():
#     n, direction = input().split()
#     n = int(n)
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     operations = []
#     # Поворот матрицы на 90 градусов по часовой стрелке
#     if direction == "R":
#         for i in range(n // 2 + n % 2):
#             for j in range(n):
#                 if matrix[i][j] != matrix[n - i - 1][j]:
#                     operations.append([j, i, n - i - 1, j])

#     # Поворот матрицы на 90 градусов против часовой стрелки
#     elif direction == "L":
#         for i in range(n // 2 + n % 2):
#             for j in range(n):
#                 if matrix[i][j] != matrix[j][n - i - 1]:
#                     operations.append([j, n - i - 1, i, j])

#     print(f"{len(operations)}")
#     for op in operations:
#         print(*op)

# Задача 5
# def main():
#     n = int(input())

#     forest = [list(input()) for _ in range(n)]

#     n = len(forest)
#     dp = [[0] * 3 for _ in range(n)]
#     for j in range(3):
#         if forest[0][j] == "C":
#             dp[0][j] = 1
#     if forest[0].count("W") != 3:
#         for i in range(1, n):
#             for j in range(3):

#                 if forest[i][j] == "W":
#                     continue
#                 for k in range(max(0, j - 1), min(3, j + 2)):
#                     dp[i][j] = max(dp[i][j], dp[i - 1][k] + (forest[i][j] == "C"))

#     print(max(dp[-1]))
