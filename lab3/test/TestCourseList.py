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

    def test_remove(self):
        """测试删除课程"""
        course = Obj.CourseList()
        course.add('1', '2', '3', '4')
        course.remove('1')
        self.assertEquals(course.courses, [])

    def test_query(self):
        """测试查询课程"""
        course = Obj.CourseList()
        course.add('1', '2', '3', '4')
        self.assertEquals(course.query('1')['courseID'], '1')
        self.assertEquals(course.query('1')['courseName'], '2')
        self.assertEquals(course.query('1')['courseCredit'], '3')
        self.assertEquals(course.query('1')['courseTeacher'], '4')
        self.assertEquals(course.query('2'), None)

        # 查询全部
        course.add('2', '3', '4', '5')
        self.assertEquals(course.query(''), [{
            'courseID': '1',
            'courseName': '2',
            'courseCredit': '3',
            'courseTeacher': '4',
        }, {
            'courseID': '2',
            'courseName': '3',
            'courseCredit': '4',
            'courseTeacher': '5',
        }])

    def test_write(self):
        """测试写入文件"""
        course = Obj.CourseList()
        course.add('1', '2', '3', '4')
        course.write()
        self.assertTrue(os.path.exists(course.path))


# 运行测试
if __name__ == '__main__':
    unittest.main()
