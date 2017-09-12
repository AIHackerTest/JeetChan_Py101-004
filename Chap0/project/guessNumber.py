""" 猜数字游戏 
程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
用户输入 4 位数进行猜测，程序返回相应提示
    用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
    用户猜测后，程序返回 A 和 B 的数量
    比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
猜对或用完 10 次机会，游戏结束
"""
import random
import itertools


def getPermutations(iterable, r):
    """ 获取首位不为0全排列数 """

    listNumber = list(itertools.permutations(iterable, r))
    # 去除首位为0的数
    less_than_zero = list(filter(lambda x: x[0] > 0, listNumber))
    return less_than_zero


def guessNumbers():
    """ 猜数字 """

    mesg = '请输入一个四位数字，每个数位上的数字不重复，且首位数字不为零，如 1942。'

    less_than_zero = getPermutations(range(10), 4)
    toList = list(map(list, less_than_zero))

    # 随机获取数组中的一个4位数
    secretNumber = list(random.choice(less_than_zero))
    # 非测试时请注释下面语句
    #print('secretNumber:', secretNumber, end='')
    print(mesg)
    results = []
    frequency = 1
    listGuess = []
    while frequency < 11:
        results.clear()
        strGuess = input()
        listGuess = list(strGuess)
        # 验证数字
        if strGuess.isdigit():
            # 验证全排列数
            if list(map(int, listGuess)) not in toList:

                print(mesg)
                continue
        else:
            print('你输入的不是数字，' + mesg)
            continue

        for i, val in enumerate(listGuess):
            intVal = int(val)
            if intVal in secretNumber:
                if secretNumber.index(intVal) == i:
                    results.append('A')
                else:
                    results.append('B')
        countA = results.count('A')
        if countA == 4:
            print("AAAA，恭喜，你猜对了！游戏结束。")
            break
        countB = results.count('B')
        print(countA, 'A', countB, 'B', end='')
        if frequency == 10:
            print('游戏结束。正确答案是：' + ''.join(list(list(map(str, secretNumber)))))
        else:
            print('已猜{0}次，还有{1}次机会'.format(frequency, 10 - frequency))

        frequency += 1


guessNumbers()