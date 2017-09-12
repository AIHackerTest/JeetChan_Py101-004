""" 文件操作 """

### @export "setup"
import fake_input
input, input = fake_input.create(['ex15_sample.txt'])

### @export "code"
from sys import argv

script, filename = argv

# 查询文档，open方法可指定encoding，如乱码可设置该参数
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


