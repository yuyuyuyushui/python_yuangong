import os, sys


def Buy(busyness_list, money):
    puchar_list = []
    while True:
        num = input("\n请输入你想购买的商品序号")
        if num.isdigit():  # 判断输入是否是数字
            num = int(num)
            if num>=0 and num<len(busyness_list)+1 :
                if int(busyness_list[num][2]) < money:
                    print('你购买的商品是', busyness_list[num][1])
                    puchar_list.append(busyness_list[num][1])
                    money = money - int(busyness_list[num][2])
                    flag_buy = 0
                    while not flag_buy:
                        x = input("\n你是否继续购买:Y/N")
                        if x == 'Y':
                            flag_buy = 1
                        if x == 'N':
                            return puchar_list
                        else:
                            print("请输入正确的填写")
                            continue
                else:
                    print("余额不足，请重新选择，或充值")
                    continue
            else:
                print("请输入合适的数字购买")
                continue
        elif num == 'q':
                return puchar_list
salary = input("请输入你的工资:")
if salary.isdigit():
    salary = int(salary)
else:
    print("请输入正数")
    exit()
while True:
    line_list = []
    accunt = input('\n请输入你的账号:')
    passwd = input("\n请输入的密码:")
    if accunt=='admin' and passwd=='123456':
        with open('商品列表','r') as f:
            for line in f:
                print(line.strip(""))
                line = line.strip("\n").split(' ')
                line_list.append(line)
            print(line_list)
            flag = Buy(line_list, salary)
            if flag:
                print("ok")
                new = ','.join(flag)
                print("购买的产品列表：%s"%new)
                exit()
            else:
                print("请购买你想要的产品")
    if accunt == "q" or passwd =="q":
        exit()
    else:
        continue
