
""" 猜数字草稿 """
import itertools
import random
# from functools import reduce

# s = [0, 1, 2]
# s = []
# for i in range(10):
#   s.append(i)

# list1 = list(itertools.combinations('abc', 2))
# print(list1)

list2 = list(itertools.permutations(range(10), 4))

# print(list2)
# print(type(list2[0]))
# print(type(list2))

less_than_zero = list(filter(lambda x: x[0] > 0, list2))
#print(random.choice(less_than_zero))
#print(type(random.choice(less_than_zero)))
#content = ''.join(list(less_than_zero[0]))
#print(content)
strList = ''.join(list(list(map(str, random.choice(less_than_zero)))))
print(int(strList))
# print(type(strList))

guessesTaken = 0
while True:
    for frequency in range(1, 11):
        print(frequency)
        guessesTaken = frequency
    if (guessesTaken == 10):
        break
"""
li = [11, 22, 33]

product = reduce((
    lambda thousands, hundreds, tens, ones: thousands * 10**3 + hundreds * 10**2 + tens * 10**1 + ones
), [1, 2, 3, 4])
print(product)

n = less_than_zero[0]
for i in n:
    print(i)
print(sum([i**len(n) for i in n]))

test_list = [1, 3, 4, 'Hongten', 3, 6, 23, 'hello', 2]
for i in range(len(test_list)):
    print(test_list[i], end=',')

"""