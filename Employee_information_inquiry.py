def read_text():
    """
    读取文本信息
    :return 字典结构的员工信息:
    """
    culum = ['id','name', 'age', 'phone', 'dept',  'enroll_date']
    dict = {}
    for i in culum:
        dict[i] = []
    with open('员工信息表', 'r',encoding='utf-8') as f:
        for i in f:
            for j, k in enumerate(i.strip('\n').split(',')):
                dict[culum[j]].append(k)
    return dict
def greater_than(condition_name,condition_tit):
    data_dict = read_text()
    if condition_name in data_dict:
        choice_list = []
        for data_index, data_list in enumerate(data_dict[condition_name]):# 获取输入键对应的值
            if int(data_list) > int(condition_tit):
                row_list = []
                for row in data_dict: #遍历数组的每一行
                    row_list.append(data_dict[row][data_index]) #获取每一行的值
                choice_list.append(row_list)
        print(choice_list)
        return choice_list
    else:
        print('你输入的参数有问题')
def less_than(condition_name,condition_tit):
    data_dict = read_text()
    if condition_name in data_dict:
        choice_list = []
        for data_index, data_list in enumerate(data_dict[condition_name]):  # 获取输入键对应的值
            if int(data_list) < int(condition_tit):
                row_list = []
                for row in data_dict:  # 遍历数组的每一行
                    row_list.append(data_dict[row][data_index])  # 获取每一行的值
                choice_list.append(row_list)
        print(choice_list)
        return choice_list
    else:
        print('你输入的参数有问题')
def equel_to(condition_name,condition_tit):
    data_dict = read_text()
    if condition_name in data_dict:
        choice_list = []
        for data_index, data_list in enumerate(data_dict[condition_name]):  # 获取输入键对应的值
            if int(data_list) == int(condition_tit):
                row_list = []
                for row in data_dict:  # 遍历数组的每一行
                    row_list.append(data_dict[row][data_index])  # 获取每一行的值
                choice_list.append(row_list)
        print(choice_list)
        return choice_list
    else:
        print('你输入的参数有问题')
def vegue(condition_name,condition_tit):
    data_dict = read_text()
    if condition_name in data_dict:
        choice_list = []
        for data_index, data_list in enumerate(data_dict[condition_name]):  # 获取输入键对应的值
            if condition_tit in data_list :
                row_list = []
                for row in data_dict:  # 遍历数组的每一行
                    row_list.append(data_dict[row][data_index])  # 获取每一行的值
                choice_list.append(row_list)
        print(choice_list)
        return choice_list
    else:
        print('你输入的参数有问题')
def condition_screening(condition_val):#根据where后的值来进行条件查询
    """
    做where的筛选，返回筛选值
    :param condition_val:
    :return:
    """
    comparison_dict = {'>':greater_than,
                       '<':less_than,
                       '=':equel_to,
                      'like':vegue}
    list_mess = []
    for comparison in comparison_dict:  #循环字典的键
        if comparison in condition_val: #判断where条件中是否有这些字段
            condition_list = condition_val.split(comparison)#以判定的比较符做分割返回比较名和比较值
            condition_name, condition_tit = [i.strip() for i in condition_list]#取干净的比较值
            return comparison_dict[comparison](condition_name,condition_tit)
        else:
            print('')
def add_message():
    pass
def delet_message():
    pass
def modify_message():
    pass
def query_message(cmd_list):
    print(cmd_list)
    if 'where' in cmd_list :
        list_where = cmd_list[-3:]
        listmess = condition_screening(list_where)
        print(listmess)
        list_work = read_text()
        list_1 = []
        for num in listmess:
            list_2 = []
            for i in list_work:
                list_2.append(list_work[i][num])
            list_1.append(list_2)
        print(list_1)
def view(cmd_list):
    """
    传入列表并判断
    :param cmd_list:
    :return:
    """


def main():
    """
    主函数，主逻辑流程
    :return:
    """
    accute = {
        1: '增加',
        2: '删除',
        3: "修改",
        4: "查找"
    }
    route_operation = {
        'add': add_message,
        'delet': delet_message,
        'update': modify_message,
        'select': query_message
    }
    while True:
        cmd = input("请输入》》").strip('\n')

        #operation_list = ['add', 'delet', 'update', 'select']
        if not cmd: continue
        else:

            if cmd.split(' ')[0] in route_operation:
                query_left, query_right = cmd.split('where')
                print(repr(query_left),query_right)
                condition_screening(query_right)
            else:
                print('你输入的数据有问题')
if __name__ == '__main__':
    main()