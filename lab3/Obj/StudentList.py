from util import *


class StudentList:
    """学生列表"""

    def __init__(self):
        self.path = './data/student.json'

        # 读取文件
        self.students = []
        self.load()

    def add(self, studentID, studentName, studentSex, studentAge, studentClass):
        """
        添加学生
        :param studentID: 学号
        :param studentName: 姓名
        :param studentSex: 性别
        :param studentAge: 年龄
        :param studentClass: 班级
        """
        self.students.append({
            'studentID': studentID,
            'studentName': studentName,
            'studentSex': studentSex,
            'studentAge': studentAge,
            'studentClass': studentClass,
        })

    def load(self):
        """加载文件"""
        self.students = read_json(self.path)
        if self.students is None:
            self.students = []

    def write(self):
        """写入文件"""
        if not os.path.exists('./data'):
            os.mkdir('./data')
        write_json(self.path, self.students)