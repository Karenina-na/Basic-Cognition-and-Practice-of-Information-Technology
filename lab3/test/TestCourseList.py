import unittest
import Obj
import os


class TestCourseList(unittest.TestCase):
    """测试课程列表"""


    def setUp(self):
        pass

    def tearDown(self):
        """清理文件"""
        path = Obj.CourseList().path
        if os.path.exists(path):
            os.remove(path)

    def test_add(self):
        """测试添加课程"""
        course = Obj.CourseList()
        course.add('1', '2', '3', '4')
        self.assertEquals(course.courses[0]['courseID'], '1')
        self.assertEquals(course.courses[0]['courseName'], '2')
        self.assertEquals(course.courses[0]['courseCredit'], '3')
        self.assertEquals(course.courses[0]['courseTeacher'], '4')

    def test_write(self):
        """测试写入文件"""
        course = Obj.CourseList()
        course.add('1', '2', '3', '4')
        course.write()
        self.assertTrue(os.path.exists(course.path))


# 运行测试
if __name__ == '__main__':
    unittest.main()
