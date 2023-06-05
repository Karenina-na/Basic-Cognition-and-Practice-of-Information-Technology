def showList(empList):
    print('*' * 5, '员工列表', '*' * 5)
    print('编号\t\t姓名\t\t性别\t\t地址\t\t生日')
    print('=' * 120)
    for emp in empList:
        print(emp['id'], '\t', emp['name'], '\t', emp['sex'], '\t', emp['address'], '\t', emp['birthday'])

    print('=' * 120)


if __name__ == "__main__":
    emp = {'id': 1, 'name': '张飞', 'sex': '男', 'address': '北京', 'birthday': '1998-12-12'}

    empList = []
    empList.append(emp)
    empList.append(
        {
            'id': 2,
            'name': '关羽',
            'sex': '男',
            'address': '上海',
            'birthday': '1998-12-12'
        }
    )
    empList.append(
        {
            'id': 3,
            'name': '刘备',
            'sex': '男',
            'address': '广州',
            'birthday': '1998-12-12'
        }
    )
    showList(empList)

    name = input('请输入员工姓名：')
    # 查找是否有员工信息
    for emp in empList:
        if emp['name'] == name:
            print('编号\t\t姓名\t\t性别\t\t地址\t\t生日')
            print('=' * 120)
            print(emp['id'], '\t', emp['name'], '\t', emp['sex'], '\t', emp['address'], '\t', emp['birthday'])
            break
        if emp == empList[-1]:
            print('没有找到员工信息')

    id = int(input('请输入需要删除员工编号：'))

    for emp in empList:
        if emp['id'] == id:
            empList.remove(emp)
            break
        if emp == empList[-1]:
            print('没有找到员工信息')
    print("删除后的员工信息")
    showList(empList)

    id = int(input('请输入需要修改员工编号：'))
    for emp in empList:
        if emp['id'] == id:
            emp['address'] = input('请输入员工地址：')
            emp['birthday'] = input('请输入员工生日：')
            break
        if emp == empList[-1]:
            print('没有找到员工信息')
    print("修改后的员工信息")
    showList(empList)