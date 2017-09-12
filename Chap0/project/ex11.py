""" 方法返回方法？待学习 """

### @export "fake"
import fake_input

# 返回Function元组？？此处不明白
input, input = fake_input.create(['38', '6\'2"', '180lbs'])

### @export "code"
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# 字符串前加‘f’格式化，大括号内直接写变量
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

