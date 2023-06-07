from util import *


class CourseList:
    """课程列表"""

    def __init__(self):
        self.path = './data/course.json'

        # 读取文件
        self.courses = []
        self.load()

    def add(self, courseID, courseName, courseCredit, courseTeacher):
        """
        添加课程
        :param courseID: 课程ID
        :param courseName: 课程名
        :param courseCredit: 学分
        :param courseTeacher: 教师
        """
        self.courses.append({
            'courseID': courseID,
            'courseName': courseName,
            'courseCredit': courseCredit,
            'courseTeacher': courseTeacher,
        })

    def load(self):
        """加载文件"""
        self.courses = read_json(self.path)
        if self.courses is None:
            self.courses = []

    def write(self):
        """写入文件"""
        if not os.path.exists('./data'):
            os.mkdir('./data')
        write_json(self.path, self.courses)