# 第 3 天练习（2026-09-07）：列表 list
# 知识讲解在对话框里，这里只放任务。
# 老规矩：先写中文步骤（伪代码）再写代码。
# 运行：右键 -> Run 'practice3'（看不到文件就先右键项目文件夹 -> Reload from Disk）

# ---- 任务 1：名字列表（热身） ----
# 建一个列表存 3 个朋友/同学的名字
# 打印：第 1 个名字、最后 1 个名字、一共几个人
list = ["小a","小b","小c"]
print(list[0],list[2],"一共有",len(list),"人")
# ---- 任务 2：平均分（把昨天的累加器用到列表上） ----
# scores = [88, 95, 60, 77, 100]
# 用 for + 累加器算出平均分并打印（先别用 sum()，练手动累加）
answer = 0
scores = [88, 95, 60, 77, 100]
for n in scores:
    answer += n
print(answer/len(scores))
# ---- 任务 3：找最高分（"先假设第 1 个最大"套路） ----
# 用同一个 scores，用 for 找出最高分并打印
scores = [88, 95, 60, 77, 100]
bigger = scores[0]
for n in scores:
    if n > bigger:
        bigger = n
print(bigger)
# ---- 任务 4（选做）：输入 3 个数存进列表 ----
# 让用户输入 3 个数字，用 append 存进空列表，最后打印列表和总和
#考虑的解法是让用户一次输入三个数字并提示用空格隔开
#将输入存入列表并输出总和
#将输入数据进行split操作后直接存入数组
#遍历数组，将数据转换成数学数字，判断符合条件同时转移到空列表同时得到每个数据
#最后累加输出
while True:
    empty = []
    total = 0
    text = input("请输入任意三个数字，并使用空格隔开")
    new_list = text.split()
    try:
        for n in new_list:
            empty.append(int(n))
    except ValueError:
        print("请不要输入除数字外的文本")
        continue
    for i in empty:
        total += i
    print(total)
    break



