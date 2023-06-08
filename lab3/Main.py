# 基于pyqt5的学生信息选课管理系统

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
from UI.MainUI import Ui_StudentManagement
from Obj import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_StudentManagement()
        self.ui.setupUi(self)

        # 挂载事件
        self.ui.studentButton.clicked.connect(self.studentRegister)
        self.ui.deleteStudentButton.clicked.connect(self.removeStudent)
        self.ui.studentButton_3.clicked.connect(self.queryStudent)
        self.ui.courseButton.clicked.connect(self.courseRegister)

        # 学生管理类
        self.studentManager = StudentList()
        # 课程管理类
        self.courseManager = CourseList()
        # 选课管理类
        self.scManager = SelectCourseList()

        # 加载信息
        self.studentManager.load()
        self.courseManager.load()
        self.scManager.load()

    def studentRegister(self):
        """
        输入学生信息，注册学生
        """
        # 获取学生信息
        studentID = self.ui.ID_input.text()
        studentName = self.ui.Name_input.text()
        studentGender = None
        if self.ui.manButton.isChecked():
            studentGender = "男"
        elif self.ui.womanButton.isChecked():
            studentGender = "女"
        studentAge = self.ui.Age_input.text()
        studentClass = self.ui.Class_input.text()

        # 如果有空值，弹出警告
        if studentID == "":
            self.ui.ID_input.setFocus()
            self.ui.ID_input.setStyleSheet("border: 1px solid red;")
            self.ui.lineEdit.setText("不能为空")
            self.ui.lineEdit.setStyleSheet("color: red;")
            return
        else:
            self.ui.ID_input.setStyleSheet("")
        if studentName == "":
            self.ui.Name_input.setFocus()
            self.ui.Name_input.setStyleSheet("border: 1px solid red;")
            self.ui.lineEdit.setText("不能为空")
            self.ui.lineEdit.setStyleSheet("color: red;")
            return
        else:
            self.ui.Name_input.setStyleSheet("")
        if studentGender is None:
            QMessageBox.warning(self, "错误", "性别不能为空")
            return
        if studentAge == "":
            self.ui.Age_input.setFocus()
            self.ui.Age_input.setStyleSheet("border: 1px solid red;")
            self.ui.lineEdit.setText("不能为空")
            self.ui.lineEdit.setStyleSheet("color: red;")
            return
        else:
            self.ui.Age_input.setStyleSheet("")
        if studentClass == "":
            self.ui.Class_input.setFocus()
            self.ui.Class_input.setStyleSheet("border: 1px solid red;")
            self.ui.lineEdit.setText("不能为空")
            self.ui.lineEdit.setStyleSheet("color: red;")
            return
        else:
            self.ui.Class_input.setStyleSheet("")

        # 注册学生
        self.studentManager.add(studentID, studentName, studentGender, studentAge, studentClass)

        # 更改提示
        self.ui.lineEdit.setText("注册成功")
        self.ui.lineEdit.setStyleSheet("color: green;")

    def removeStudent(self):
        """
        输入学号，删除学生
        """

        # 获取学号信息
        studentID = self.ui.ID_input_7.text()

        # 如果有空值，弹出警告
        if studentID == "":
            self.ui.ID_input_7.setFocus()
            self.ui.ID_input_7.setStyleSheet("border: 1px solid red;")
            self.ui.deleteStudentState.setText("不能为空")
            self.ui.deleteStudentState.setStyleSheet("color: red;")
            return

        # 删除学生
        flag = self.studentManager.remove(studentID)

        if flag:
            # 更改提示
            self.ui.deleteStudentState.setText("删除成功")
            self.ui.deleteStudentState.setStyleSheet("color: green;")
        else:
            # 更改提示
            self.ui.deleteStudentState.setText("不存在")
            self.ui.deleteStudentState.setStyleSheet("color: red;")

    def queryStudent(self):
        """
        输入学号，查询学生
        """

        # 获取学号信息
        studentID = self.ui.ID_input_2.text()

        # 查询学生
        student = self.studentManager.query(studentID)

        if studentID == "":
            # 查询全部
            if not student:
                # 更改提示
                self.ui.textBrowser.setText("---------无学生信息---------")
                self.ui.textBrowser.setStyleSheet("color: red;")
            else:
                # 更改提示，组装信息
                output = "----------学生信息----------\n"
                for stu in student:
                    # 学号预留10位，姓名预留4位，性别预留1位，年龄预留3位，班级预留3位
                    s = stu['studentID'] + " " * (11 - len(stu['studentID'])) + \
                        stu['studentName'] + "  " * (5 - len(stu['studentName'])) + \
                        stu['studentSex'] + " " + \
                        stu['studentAge'] + " " * (3 - len(stu['studentAge'])) + \
                        stu['studentClass'] + " " * (3 - len(stu['studentClass'])) + "\n"
                    output += s
                self.ui.textBrowser.setText(output)
                self.ui.textBrowser.setStyleSheet("color: black;")
        else:
            # 查询单个
            if student is None:
                # 更改提示
                self.ui.textBrowser.setText("-------学生信息不存在-------")
                self.ui.textBrowser.setStyleSheet("color: red;")
            else:
                # 组装信息
                output = "----------学生信息----------\n"
                # 学号预留10位，姓名预留4位，性别预留1位，年龄预留3位，班级预留3位
                s = student['studentID'] + " " * (11 - len(student['studentID'])) + \
                    student['studentName'] + "  " * (5 - len(student['studentName'])) + \
                    student['studentSex'] + " " + \
                    student['studentAge'] + " " * (3 - len(student['studentAge'])) + \
                    student['studentClass'] + " " * (3 - len(student['studentClass'])) + "\n"
                output += s
                self.ui.textBrowser.setText(output)
                self.ui.textBrowser.setStyleSheet("color: black;")

    def courseRegister(self):
        """
        输入课程信息，注册课程
        """

        # 获取课程信息
        courseID = self.ui.courseID_input.text()
        courseName = self.ui.courseName_input.text()
        courseCredit = self.ui.courseCredit_input.text()
        courseTeacher = self.ui.courseTeacher_input.text()

        # 如果有空值，弹出警告
        if courseID == "":
            self.ui.courseID_input.setFocus()
            self.ui.courseID_input.setStyleSheet("border: 1px solid red;")
            self.ui.courseState.setText("不能为空")
            self.ui.courseState.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseID_input.setStyleSheet("")
        if courseName == "":
            self.ui.courseName_input.setFocus()
            self.ui.courseName_input.setStyleSheet("border: 1px solid red;")
            self.ui.courseState.setText("不能为空")
            self.ui.courseState.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseName_input.setStyleSheet("")
        if courseCredit == "":
            self.ui.courseCredit_input.setFocus()
            self.ui.courseCredit_input.setStyleSheet("border: 1px solid red;")
            self.ui.courseState.setText("不能为空")
            self.ui.courseState.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseCredit_input.setStyleSheet("")
        if courseTeacher == "":
            self.ui.courseTeacher_input.setFocus()
            self.ui.courseTeacher_input.setStyleSheet("border: 1px solid red;")
            self.ui.courseState.setText("不能为空")
            self.ui.courseState.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseTeacher_input.setStyleSheet("")

        # 注册课程
        self.courseManager.add(courseID, courseName, courseCredit, courseTeacher)

        # 更改提示
        self.ui.courseState.setText("注册成功")
        self.ui.courseState.setStyleSheet("color: green;")

    def removeCourse(self):
        """
        输入课程号，删除课程
        """

        # 获取课程号信息
        courseID = self.ui.courseID_input_2.text()

        # 如果有空值，弹出警告
        if courseID == "":
            self.ui.courseID_input_2.setFocus()
            self.ui.courseID_input_2.setStyleSheet("border: 1px solid red;")
            self.ui.deleteCourseState.setText("不能为空")
            self.ui.deleteCourseState.setStyleSheet("color: red;")
            return

        # 删除课程
        flag = self.courseManager.remove(courseID)

        if flag:
            # 更改提示
            self.ui.deleteCourseState.setText("删除成功")
            self.ui.deleteCourseState.setStyleSheet("color: green;")
        else:
            # 更改提示
            self.ui.deleteCourseState.setText("不存在")
            self.ui.deleteCourseState.setStyleSheet("color: red;")


    def queryCourse(self):
        pass

    def SCRegister(self):
        pass

    def removeSC(self):
        pass


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    # 创建主窗口
    main = Main()
    # 显示窗口
    main.show()

    sys.exit(app.exec_())
