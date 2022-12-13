# Получение первых пяти чисел, подобных числу Рамануджана
# 1729 = 1^3 + 12^3 = 9^3 + 10^3

from array import *

result = array('i', [100000, 100000, 100000, 100000, 100000])
for i in range(1, 50):
  for j in range(1, 50):
    for k in range(1, 50):
      for l in range(1, 50):
        if i**3 + j**3 == k**3 + l**3 and (i != k and i != l):
          num = i**3 + j**3
          for m in range(5):
            if num < max(result) and result.count(
                num) == 0 and result[m] == max(result):
              result[m] = num
              break
for i in result:
  print(i)
