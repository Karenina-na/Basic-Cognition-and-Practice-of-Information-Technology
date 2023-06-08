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

        self.ui.studentButton.clicked.connect(self.studentRegister)

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
            return
        else:
            self.ui.ID_input.setStyleSheet("")
        if studentName == "":
            self.ui.Name_input.setFocus()
            self.ui.Name_input.setStyleSheet("border: 1px solid red;")
            return
        else:
            self.ui.Name_input.setStyleSheet("")
        if studentGender is None:
            QMessageBox.warning(self, "错误", "性别不能为空")
            return
        if studentAge == "":
            self.ui.Age_input.setFocus()
            self.ui.Age_input.setStyleSheet("border: 1px solid red;")
            return
        else:
            self.ui.Age_input.setStyleSheet("")
        if studentClass == "":
            self.ui.Class_input.setFocus()
            self.ui.Class_input.setStyleSheet("border: 1px solid red;")
            return
        else:
            self.ui.Class_input.setStyleSheet("")

        print(studentID, studentName, studentGender, studentAge, studentClass)

    def removeStudent(self):
        pass

    def queryStudent(self):
        pass

    def courseRegister(self):
        pass

    def removeCourse(self):
        pass

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
