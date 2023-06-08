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

    def remove(self, studentID, courseID):
        """
        删除选课信息
        :param studentID: 学生ID
        :param courseID: 课程ID
        """
        for select in self.select:
            if select['studentID'] == studentID and select['courseID'] == courseID:
                self.select.remove(select)
                return True
        return False

    def query(self, studentID):
        """
        查询选课信息
        :param studentID: 学生ID
        """
        if studentID == "":
            return self.select
        cho = []
        for select in self.select:
            if select['studentID'] == studentID:
                cho.append(select)
        return cho

    def removeByStudentID(self, studentID):
        """
        删除选课信息
        :param studentID: 学生ID
        """
        self.select = [select for select in self.select if select['studentID'] != studentID]
        return True

    def removeByCourseID(self, courseID):
        """
        删除选课信息
        :param courseID: 课程ID
        """
        self.select = [select for select in self.select if select['courseID'] != courseID]
        return True

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