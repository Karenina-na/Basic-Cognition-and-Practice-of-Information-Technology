def showList(studentList):
    print('*' * 5, '学生列表', '*' * 5)
    print('编号\t\t姓名\t\t性别\t\t地址\t\t生日')
    print('=' * 120)
    for stu in studentList:
        print(stu['id'], '\t', stu['name'], '\t', stu['sex'], '\t', stu['address'], '\t', stu['birthday'])

    print('=' * 120)


if __name__ == "__main__":
    emp = {'id': 1, 'name': '张飞', 'sex': '男', 'address': '北京', 'birthday': '1998-12-12'}

    print('获取学生编号:', emp['id'])
    print('获取学生姓名:', emp['name'])
    print('获取学生性别:', emp['sex'])
    print('获取学生地址:', emp['address'])
    print('获取学生生日:', emp['birthday'])

    empList = [
        {'id': 1, 'name': '张飞', 'sex': '男', 'address': '北京', 'birthday': '1998-12-12'},
        {'id': 2, 'name': '马超', 'sex': '男', 'address': '汉中', 'birthday': '1998-11-12'},
        {'id': 3, 'name': '关羽', 'sex': '男', 'address': '运城', 'birthday': '1998-09-12'},
        {'id': 4, 'name': '赵云', 'sex': '男', 'address': '常山', 'birthday': '1998-12-10'},
        {'id': 5, 'name': '黄忠', 'sex': '男', 'address': '长沙', 'birthday': '1998-12-09'},
        {'id': 6, 'name': '吕布', 'sex': '男', 'address': '绥德', 'birthday': '1998-12-06'},
    ]

    showList(empList)
    student = {
        'id': input('输入学生编号：'),
        'name': input('输入学生姓名：'),
        'sex': input('输入学生性别：'),
        'address': input('输入学生地址：'),
        'birthday': input('输入学生生日：')
    }

    empList.append(student)

    print('查看添加完成的学生列表数据')

    showList(empList)