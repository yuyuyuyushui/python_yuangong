def read():
    yuangong_list = []
    with open("员工信息表", 'r', encoding='utf-8') as f:
        for i in f:
            yuangong_list.append(i.strip(' \n').split(','))
    print(yuangong_list)
    return yuangong_list

def add_message(list):
    with open("员工信息表",'a',encoding='utf-8') as f:
        a = ','.join(list)
        f.write('\n'+a)
    return 1
def delet_message():
    pass
def modify_message():
    pass
def query_message():
    pass

if __name__ == '__main__':
    accute = {
        1: '增加',
        2: '删除',
        3: "修改",
        4: "查找"
    }
    caluate = {
        1:add_message,
        2:delet_message,
        3:modify_message,
        4:query_message
    }
while True:
    for i in accute:
        print(i,accute[i])
    x = input('请输入你想做的选择')
    if int(x) in caluate:
        flag = False
        while True:
            add_list = input("请输入你想增加的，例如：x1 x2 x3 》》").strip().split(' ')
            if len(add_list) == 5:
                telp = add_list[2]
                list = read()
                ind = list.pop()[0]
                for i in list:
                    if telp in i:
                        print("你增加的号码已存在")
                        flag = True
                        break
                if not flag:
                    add_list.insert(0, str(int(ind)+1))
                    caluate[int(x)](add_list)
            if len(add_list) == 1:
                break
    else:
        print('你的选择有错，请重新选择')