china_map = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}
china_m = china_map
china_m_list = []
while True:
    for i in china_m:
        print(i)
    key = input("请输入你想访问的对象：").strip()
    if key in china_m:
        china_m_list.append(china_m)
        china_m = china_m[key] #进入下一级菜单,赋值给变量
    elif key == 'b':
        print('返回上一级菜单')
        if china_m_list:
            china_m = china_m_list.pop()
        else:
            print("已是顶层")
            china_m = china_map
    else:
        print('请输入正确的地址')
