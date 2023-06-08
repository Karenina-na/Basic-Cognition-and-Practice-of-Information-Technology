from util import *


class SelectCourseList:
    """选课类"""

    def __init__(self):
        self.path = './data/select.json'

        # 读取文件
        self.select = []
        self.load()

    def add(self, studentID, courseID):
        """
        添加选课信息
        :param studentID: 学生ID
        :param courseID: 课程ID
        """
        self.select.append({
            'studentID': studentID,
            'courseID': courseID
        })

    def load(self):
        """加载文件"""
        self.select = read_json(self.path)
        if self.select is None:
            self.select = []

    def write(self):
        """写入文件"""
        if not os.path.exists('./data'):
            os.mkdir('./data')
        write_json(self.path, self.select)