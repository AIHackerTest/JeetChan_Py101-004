## 程序使用说明

* 程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942。

* 用户输入 4 位数进行猜测，程序返回相应提示
用 
  - A 表示数字和位置都正确，用 B 表示数字正确但位置错误
  - 用户猜测后，程序返回 A 和 B 的数量
  - 比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
* 猜对或用完 10 次机会，游戏结束

测试时请解除代码第33行注释，``` print('secretNumber:', secretNumber, end='') ``` ，以便知道我们将要猜的数字。运行代码，``` python guessNumber.py ``` ，根据提示猜数字，以实际路劲为准，见下图，图片有标注说明：


![](https://github.com/JeetChan/LearnPythontheHardWay/blob/master/image/guessNumber.png)

## 参考

[随机数](https://docs.python.org/3.6/library/random.html#random.choice)

[Permutation](https://en.wikipedia.org/wiki/Permutation)

[python使用递归解决全排列数字示例](http://www.jb51.net/article/46631.htm)

[Map, Filter and Reduce](http://book.pythontips.com/en/latest/map_filter.html)

[Lambdas](https://docs.python.org/3.6/reference/expressions.html#lambda)

[itertools.permutations](https://docs.python.org/3.6/library/itertools.html#itertools.permutations)

[Python生成0-9任意4位数字组合的方法](http://www.iplaypy.com/code/algorithm/a2589.html)