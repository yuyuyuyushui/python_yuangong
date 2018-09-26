def read_text():
    """
    读取文本信息
    :return 字典结构的员工信息:
    """
    dict_message = {}
    for i in culum_list:
        dict_message[i] = []
    with open('员工信息表', 'r', encoding='utf-8') as f:
        for line_message in f:
            for index, line_val in enumerate(line_message.strip('\n').split(',')):
                dict_message[culum_list[index]].append(line_val)  #同时循环字典的键和字典的值列表
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
        return choice_list
    else:
        print('你输入的参数有问题')


def less_than(condition_name, condition_tit):
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
def save():
    with open("%s.new"%db_file,'w',encoding='utf-8') as f:
        for staff_index, staff_id in enumerate(culumes_dict['id']):
            list_date = []
            for i in culumes_dict:
                list_date.append(culumes_dict[i][staff_index])
            f.write(','.join(list_date)+'\n')
def add_message(cmd_left):
    pass
def delet_message():
    pass
def modify_message(cmd_left, query_date):  # update db set name=jkkk where age > 24
    update_name,update_val = cmd_left.split('set')[1].strip().split('=')
    culum_index = culum_list.index(update_name) #获取需要更新的字段的索引
    for staff_id in query_date:
        staff_id = staff_id[0]
        staff_index = culumes_dict['id'].index(staff_id)
        culumes_dict[update_name][staff_index] = update_val
    print(culumes_dict)
    save()


def query_message(cmd_left, query_date):
    """cmd_left = 'select age,name from db ',query_date[['2', 'Jim', '25', '13651058808', 'IT', '2011-09-01'], ['3', 'Tom', '29', '13761054698', 'IT', '2010-03-01']"""
    select_date= [i.strip() for i in cmd_left.split("from")]
    select_date = select_date[0].split(" ")[1].split(',')  # “select age,name”.split()筛选出所要选择的元素

    if  '*'in select_date:
        date_chioces = query_date

    else:
        date_chioces = []
        """从query_date中选择name,age的list[['25', 'Jim'], ['29', 'Tom'], ['40', 'Suzen'], ['32', 'Mark']]"""
        for query_line in query_date:  #遍历外层列表
            date_chioce = []
            for select_date_row in select_date:  #遍历内层的列表的序列号
                date_index = culum_list.index(select_date_row)
                date_chioce.append(query_line[date_index])
            date_chioces.append(date_chioce)
    for i in date_chioces:
        print(i)
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
        if not cmd: continue
        else:
            if cmd.split(' ')[0] in route_operation:
                if 'where' in cmd:
                    query_left, query_right = cmd.split('where')
                    query_data = condition_screening(query_right)
                else:
                    query_data = []
                    for index, val in enumerate(culumes_dict['id']):  # 将键值对格式转换成嵌套列表
                        row_list = []
                        for row in culumes_dict:
                            row_list.append(culumes_dict[row][index])
                        query_data.append(row_list)

                    query_left = cmd.strip()
                b = cmd.split(' ')
                if cmd.split()[0] == 'add':
                    add_message(query_left.strip())
                else:
                    route_operation[b[0]](query_left.strip(), query_data)
            else:
                print('你输入的数据有问题')
if __name__ == '__main__':
    global culum_list, culumes_dict
    db_file = 'new_yuangong'
    culum_list = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    culumes_dict = read_text()
    main()