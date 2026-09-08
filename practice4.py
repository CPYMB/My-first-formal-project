# 第 4 天练习（2026-09-08）：函数 def
# 知识讲解在对话框里，这里只放任务。
# 老规矩：先写中文步骤（伪代码）再写代码。
# 运行：右键 -> Run 'practice4'（看不到文件就先右键项目文件夹 -> Reload from Disk）

# ---- 任务 1：打招呼函数（热身） ----
def greet(name):
    print(f"你好，{name}")
name = input("输入你的名字: ")
greet(name)

# ---- 任务 2：加法函数 ----
def add(a, b):
    return a + b
a = int(input("请输入第一个数字"))
b = int(input("请输入第二个数字"))
print(add(a, b))

# ---- 任务 3：判断质数函数（修正版） ----
def is_prime(n):
    if n < 2:                                    # 0 和 1 不是质数
        return False
    for i in range(2, int(n ** 0.5) + 1):        # 从 2 试到 √n
        if n % i == 0:
            return False                         # 找到一个因数 → 不是质数
    return True                                  # 全部试完 → 是质数

info = int(input("请输入任意数字："))
if is_prime(info):
    print(f"数字{info}是质数")
else:
    print(f"数字{info}不是质数")

# ---- 任务 4：找最大值函数（修正版） ----
def max_of_list(nums):
    biggest = nums[0]
    for x in nums:
        if x > biggest:
            biggest = x
    return biggest

text = input("请输入一串数字，用空格隔开：")
parts = text.split()
nums = []
for p in parts:
    nums.append(int(p))
print("最大的数是：", max_of_list(nums))
