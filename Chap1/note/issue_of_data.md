## 背景


- 我期待实现的效果/欲达成的目的是：读取Chap1\resource\weather_info.txt文件，把天气信息保存到dict中
- 我的系统、版本等环境配置是：Windows10；Python3.6.1


## 现象

我想实现上述效果/目的时，遇到了这样的情况：

- 输入：以逗号分隔weather_info.txt文件中的每行数据，第0个元素作为dict的Key，第1个元素作为dict的Value，保存到dict中。
- 问题：在操作完文件后，用```len()```方法读取dict的长度为2551，weather_info.txt文件的行数为2558，dict长度应和weather_info.txt文件行数不一致。

## 分析

我已经做了以下尝试：

- 尝试 0：
    - 参考：菜鸟教程，[Python 字典(Dictionary)](http://www.runoob.com/python/python-dictionary.html)
    - 判断：weather_info.txt文件有重复数据
    - 实验：通过```k in d.keys()```判断是否有重复数据，发现有七条数据重复，完整代码见[代码仓库](https://github.com/JeetChan/Py101-004/blob/master/Chap1/project/weather.py)  
![](https://raw.githubusercontent.com/JeetChan/LearnPythontheHardWay/master/image/issue_ch1_0.jpg)
    - 结论：weather_info.txt文件有重复数据，即城市名有重复，如，340行中有“河南”的天气信息，2421行中也有“河南”的天气信息。

## 方案

我推测可以有以下几种解决方案，请问大家哪种思路正确，或有其它思路建议？

- 解决思路 0：
    
    - 设想：以第一次出现为准，如，340行中有“河南”的天气信息，2421行中也有“河南”的天气信息，只把340行信息保存到字典中。
- 解决思路 1：
  - 设想：以最后一次出现为准，如，340行中有“河南”的天气信息，2421行中也有“河南”的天气信息，只把2421行信息保存到字典中。