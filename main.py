# 猜数字小游戏（deepseek辅助优化版）
# 电脑心里想一个 1~100 的整数，你来猜。每猜一次，它会告诉你猜大了还是猜小了。
import random

# 1. 电脑随机选一个 1~100 的整数作为答案
answer = random.randint(1, 100)

# 2. 范围边界：一开始炸弹可能在 1~100 之间
low = 1
high = 100
guess_count = 0          # 记下你猜了几次

print("我心里想了一个 1~100 的整数，你来猜。猜到就算你踩到炸弹！")

# 3. 一直猜，直到猜中才 break 跳出循环
while True:
    # input() 拿到的永远是“文字”，要先转成数字才能比较大小
    text = input(f"请猜一个 {low}~{high} 之间的整数：")

    # —— 情况 1：输入的不是数字 ——
    # try = 试着做，except = 万一失败了怎么办
    try:
        num = int(text)      # 试着把文字变成整数
    except ValueError:       # 变不了（比如 abc、12.5、直接按回车）
        print("请输入一个整数，不要输字母或符号。")
        continue             # 回到循环开头重新输入，这一次不算猜测

    # —— 情况 2：数字超出了当前范围 ——
    if num < low or num > high:
        print(f"要在 {low}~{high} 之间猜哦，重新来。")
        continue             # 重新输入，这一次也不算猜测

    # 走到这里说明输入合法，算一次有效猜测
    guess_count += 1

    # —— 三种结果：猜中 / 猜大 / 猜小 ——
    if num == answer:
        print(f"BOOM！你被炸了！答案是 {answer}，你一共猜了 {guess_count} 次。")
        break                # 猜中了，跳出循环，游戏结束
    elif num > answer:
        high = num - 1       # 答案肯定比 num 小，把右边界收紧
        print(f"猜大了！炸弹在 {low}~{high} 之间。")
    else:                    # num < answer
        low = num + 1        # 答案肯定比 num 大，把左边界收紧
        print(f"猜小了！炸弹在 {low}~{high} 之间。")

print("游戏结束，下次再战！")