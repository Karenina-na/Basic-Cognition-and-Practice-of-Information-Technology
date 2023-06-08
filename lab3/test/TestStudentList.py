import unittest
import Obj
import os


class TestStudentList(unittest.TestCase):
    """测试学生列表"""

    def setUp(self):
        pass

    def tearDown(self):
        """清理文件"""
        path = Obj.StudentList().path
        if os.path.exists(path):
            os.remove(path)

    def test_add(self):
        """测试添加学生"""
        stu = Obj.StudentList()
        stu.add('1', '2', '3', '4', '5')
        self.assertEquals(stu.students[0]['studentID'], '1')
        self.assertEquals(stu.students[0]['studentName'], '2')
        self.assertEquals(stu.students[0]['studentSex'], '3')
        self.assertEquals(stu.students[0]['studentAge'], '4')
        self.assertEquals(stu.students[0]['studentClass'], '5')

    def test_remove(self):
        """测试删除学生"""
        stu = Obj.StudentList()
        stu.add('1', '2', '3', '4', '5')
        self.assertTrue(stu.remove('1'))
        self.assertFalse(stu.remove('1'))

    def test_write(self):
        """测试写入文件"""
        stu = Obj.StudentList()
        stu.add('1', '2', '3', '4', '5')
        stu.write()
        self.assertTrue(os.path.exists(stu.path))


# 运行测试
if __name__ == '__main__':
    unittest.main()
