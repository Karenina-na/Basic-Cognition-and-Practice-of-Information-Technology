import unittest
import Obj
import os


class TestSelectCourseList(unittest.TestCase):
    """测试选课类"""


    def setUp(self):
        pass

    def tearDown(self):
        """清理文件"""
        path = Obj.SelectCourseList().path
        if os.path.exists(path):
            os.remove(path)

    def test_add(self):
        """测试添加选课信息"""
        sc = Obj.SelectCourseList()
        sc.add('1', '2')
        self.assertEqual(len(sc.select), 1)
        self.assertEqual(sc.select[0]['studentID'], '1')
        self.assertEqual(sc.select[0]['courseID'], '2')

    def test_remove(self):
        """测试删除选课信息"""
        sc = Obj.SelectCourseList()
        sc.add('1', '2')
        sc.remove('1', '2')
        self.assertEqual(len(sc.select), 0)

    def test_query(self):
        """测试查询选课信息"""
        sc = Obj.SelectCourseList()
        sc.add('1', '2')
        sc.add('1', '3')
        sc.add('2', '2')
        self.assertEqual(len(sc.query('1')), 2)
        self.assertEqual(len(sc.query('2')), 1)
        self.assertEqual(len(sc.query('')), 3)

    def test_write(self):
        """测试写入文件"""
        sc = Obj.SelectCourseList()
        sc.add('1', '2')
        sc.write()
        self.assertTrue(os.path.exists(sc.path))


# 运行测试
if __name__ == '__main__':
    unittest.main()
