# zip()を学ぶぞい
"""
zipとは...
転置するための関数である。行列の転置と同じイメージ。
"""

print("===========================")
print("ex01.複数のリストを転置")
print("===========================")
print("ベースになるリストたち")
print("(li01_1)")
li01_1 = [10, 3, 8]
print(li01_1)
print("(li01_2)")
li01_2 = [5, 9, 25, 0]
print(li01_2)
print("(li01_3)")
li01_3 = [6, 3]
print(li01_3)
print()

# li01たちを転置する
print("zip(li01_1, li01_2, li01_3)でリストを転置")
li01_primary = list(zip(li01_1, li01_2, li01_3))
[print(x) for x in li01_primary]
print()

# もう一度zip(*)しても、削られた要素は戻らない
print("もう一度zip(*)しても、削られた要素は戻らない")
li01_primary = list(zip(*li01_primary))
[print(x) for x in li01_primary]
print()

# zip_longestを使ってみる
print("zip_longestを使って、削られる要素を無くす")
from itertools import zip_longest
li01_longest = list(zip_longest(li01_1, li01_2, li01_3))
[print(x) for x in li01_longest]
print()

# zip_longestを使わずにlongestを実現する
print("zip_longestを使わずにlongestを実現する")
print("　①各リストの長さをそろえてリスト(li01s)に格納")
li01s = []
max_len = max(len(li01_1), len(li01_2), len(li01_3))
for li in li01_1, li01_2, li01_3:
    li01s.append(li + [None] * (max_len - len(li)))
print(li01s)
print("　②li01sをzip(*)で転置")
li01s = list(zip(*li01s))
[print(x) for x in li01s]
print("\n\n")

print("===========================")
print("ex02.1つのリストをunpackして転置")
print("===========================")
print("ベースになるリスト(li02)")
li02 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[print(x) for x in li02]
print()

# li01を転置する
print("zip(*li02)でリストを転置")
li02 = list(zip(*li02))
[print(x) for x in li02]
print()
# タプルをlistに成型する
print("各行がタプルなのでlistに成型")
li02 = list(map(list, li02))
[print(x) for x in li02]
print()
# もう一度転置すると元に戻る
print("もう一度転置すると元にもどる")
li02 = list(zip(*li02))
[print(x) for x in li02]
print()


