with open("员工信息表",'r',encoding='utf-8') as f:
    culum = ['name','age','phone','dept','work','enroll_date']
    dict_list = {}
    for i in culum:
        dict_list[i] = []
    print(dict_list)
    for i in f:
        for k,j in enumerate(i.strip().split(',')):
            dict_list[culum[k]].append(j)
    print(dict_list)


