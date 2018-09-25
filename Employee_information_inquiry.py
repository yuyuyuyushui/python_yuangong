def read_text():
    """
    读取文本信息
    :return 字典结构的员工信息:
    """
    dict_message = {}
    for i in culum_list:
        dict_message[i] = []
    with open('员工信息表', 'r', encoding='utf-8') as f:
        for line in f:
            for index, line_val in enumerate(line.strip('\n').split(',')):
                dict_message[culum_list[index]].append(line_val)
    return dict_message

def greater_than(condition_name,condition_tit):
    data_dict = read_text()
    if condition_name in data_dict:
        choice_list = []
        for data_index, data_list in enumerate(data_dict[condition_name]):  # 获取输入键对应的值
            if int(data_list) > int(condition_tit):
                row_list = []
                for row in data_dict:  # 遍历数组的每一行
                    row_list.append(data_dict[row][data_index])  # 获取每一行的值
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
            if data_list == condition_tit:
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
    comparison_dict = {'>': greater_than,
                       '<': less_than,
                       '=': equel_to,
                      'like' : vegue}
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


def query_message(cmd_left, query_date): # cmd_left = 'select age,name from db '
    print(cmd_left, query_date)
    print(culumes_dict)
    select_date= [i.strip() for i in cmd_left.strip().split("from")]
    select_date = select_date[0].split(" ")[1].split(',')  # “select age,name”.split()筛选出所要选择的元素
    date_chioces = []
    for i in query_date:
        date_chioce = []
        for select_date_row in select_date:
            date_index = culum_list.index(select_date_row)
            date_chioce.append(i[date_index])
        date_chioces.append(date_chioce)
    print(date_chioces)
def main():
    """
    主函数，主逻辑流程
    :return:
    """
    global culumes
    culumes = read_text()
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
                query_data = condition_screening(query_right)
                b = cmd.split(' ')
                print(b[0])
                route_operation[b[0]](query_left, query_data)

            else:
                print('你输入的数据有问题')
if __name__ == '__main__':
    global culum_list, culumes_dict
    culum_list = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    culumes_dict = read_text()
    main()