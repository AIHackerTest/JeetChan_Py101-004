"""
天气查询，
输入城市名，返回该城市的天气数据；
输入指令，打印帮助文档（一般使用 h 或 help）；
输入指令，退出程序的交互（一般使用 quit 或 exit）；
在退出程序之前，打印查询过的所有城市。
"""

import os
from collections import defaultdict
import sys

dict_weather_info = defaultdict(list)
dict_histories = defaultdict(list)

help_mesg = """
1. 输入城市名，返回该城市的天气数据；
2. 输入help或h，打印帮助文档;
3. 输入history,打印查询历史;
4. 输入quit或exit，退出程序.
"""


def main():
    """
    查询天气模块方法
    """

    print(help_mesg)

    while True:
        cmd = input('>')
        if cmd in ['h', 'help']:
            print(help_mesg)
        elif cmd in ['history']:
            disply_histories()
        elif cmd in ['quit', 'exit']:
            disply_histories()
            sys.exit(0)
        else:
            try:
                weather_inquiries(cmd)
            except OSError as err:
                print("发生错误：" + str(err))
                sys.exit(0)


def weather_inquiries(city):
    """ 查询天气 """
    global dict_weather_info
    if len(dict_weather_info) == 0:

        dict_weather_info = get_weather_info()

    result = dict_weather_info.get(city)

    if result is None:
        print('暂未收录该城市天气，或城市名称有误，请重新输入。')
    else:
        print(city + ':' + result[0])
        save_histories(city, result[0])


def save_histories(city, weather):
    """ 保存历史信息 """
    dict_histories[city] = weather


def disply_histories():
    """显示历史查询信息"""
    print("历史查询信息：")
    for key, val in dict_histories.items():
        print(f'{key}： {val}')


def get_weather_info() -> dict:
    """ 从文件weather_info.txt中读取天气信息保存到词典中  """
    file_weather = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), os.pardir, 'resource',
            'weather_info.txt'))
    if os.path.isfile(file_weather):
        d = defaultdict(list)

        with open(file_weather, mode='r', encoding='UTF-8') as fh:
            lines = fh.readlines()
            for line in lines:
                k, v = line.strip().split(',')
                d[k].append(v)

    else:
        print("文件读取错误：" + file_weather)
    return d


if __name__ == "__main__":
    main()
