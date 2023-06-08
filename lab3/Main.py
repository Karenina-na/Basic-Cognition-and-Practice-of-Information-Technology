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
        self.ui.deleteCourseButton.clicked.connect(self.removeCourse)
        self.ui.courseButton_2.clicked.connect(self.queryCourse)
        self.ui.studentButton_7.clicked.connect(self.SCRegister)
        self.ui.deleteChoiceButton.clicked.connect(self.removeSC)
        self.ui.SCButton.clicked.connect(self.querySC)
        self.ui.deleteStudentChoiceID.currentIndexChanged.connect(self.updateCourseID)

        # 学生管理类
        self.studentManager = StudentList()
        # 课程管理类
        self.courseManager = CourseList()
        # 选课管理类
        self.scManager = SelectCourseList()
        # 选课学号课号列表
        self.scList = []
        # 更新选课学号课号列表
        self.update()

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
        self.update()

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
            self.scManager.removeByStudentID(studentID)
            self.update()
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
                output = "---------学生信息---------\n"
                for stu in student:
                    # 学号预留10位，姓名预留4位，性别预留1位，年龄预留3位，班级预留2位
                    s = stu['studentID'] + " " * (11 - len(stu['studentID'])) + \
                        stu['studentName'] + "  " * (4 - len(stu['studentName'])) + \
                        stu['studentSex'] + " " + \
                        stu['studentAge'] + " " * (3 - len(stu['studentAge'])) + \
                        stu['studentClass'] + " " * (2 - len(stu['studentClass'])) + "\n"
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
                # 学号预留10位，姓名预留4位，性别预留1位，年龄预留3位，班级预留2位
                s = student['studentID'] + " " * (11 - len(student['studentID'])) + \
                    student['studentName'] + "  " * (4 - len(student['studentName'])) + \
                    student['studentSex'] + " " + \
                    student['studentAge'] + " " * (3 - len(student['studentAge'])) + \
                    student['studentClass'] + " " * (2 - len(student['studentClass'])) + "\n"
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
        courseID = self.ui.ID_input_8.text()

        # 如果有空值，弹出警告
        if courseID == "":
            self.ui.ID_input_8.setFocus()
            self.ui.ID_input_8.setStyleSheet("border: 1px solid red;")
            self.ui.deleteCourseState.setText("不能为空")
            self.ui.deleteCourseState.setStyleSheet("color: red;")
            return
        else:
            self.ui.ID_input_8.setStyleSheet("")

        # 删除课程
        flag = self.courseManager.remove(courseID)

        if flag:
            self.scManager.removeByCourseID(courseID)
            self.update()
            # 更改提示
            self.ui.deleteCourseState.setText("删除成功")
            self.ui.deleteCourseState.setStyleSheet("color: green;")
        else:
            # 更改提示
            self.ui.deleteCourseState.setText("不存在")
            self.ui.deleteCourseState.setStyleSheet("color: red;")

    def queryCourse(self):
        """
        输入课程号，查询课程
        """

        # 获取课程信息
        courseID = self.ui.ID_input_4.text()

        # 查询课程
        courses = self.courseManager.query(courseID)

        if courseID == "":
            # 查询全部
            if not courses:
                # 更改提示
                self.ui.textBrowser_2.setText("------无课程信息------\n")
                self.ui.textBrowser_2.setStyleSheet("color: red;")
            else:
                # 更改提示，组装信息
                output = "-----课程信息-----\n"
                for cou in courses:
                    # 课程号预留3位，课程名预留4位，学分预留2位，执教老师预留4位
                    s = cou['courseID'] + " " * (4 - len(cou['courseID'])) + \
                        cou['courseName'] + "  " * (4 - len(cou['courseName'])) + \
                        cou['courseCredit'] + " " * (2 - len(cou['courseCredit'])) + \
                        cou['courseTeacher'] + "  " * (4 - len(cou['courseTeacher'])) + "\n"
                    output += s
                self.ui.textBrowser_2.setText(output)
                self.ui.textBrowser_2.setStyleSheet("color: black;")
        else:
            # 查询单个
            if courses is None:
                # 更改提示
                self.ui.textBrowser_2.setText("----课程信息不存在----\n")
                self.ui.textBrowser_2.setStyleSheet("color: red;")
            else:
                # 组装信息
                output = "-------课程信息-------\n"
                # 课程号预留3位，课程名预留4位，学分预留2位，执教老师预留4位
                s = courses['courseID'] + " " * (4 - len(courses['courseID'])) + \
                    courses['courseName'] + "  " * (5 - len(courses['courseName'])) + \
                    courses['courseCredit'] + " " * (3 - len(courses['courseCredit'])) + \
                    courses['courseTeacher'] + "  " * (5 - len(courses['courseTeacher'])) + "\n"
                output += s
                self.ui.textBrowser_2.setText(output)
                self.ui.textBrowser_2.setStyleSheet("color: black;")

    def SCRegister(self):
        """
        输入学号，课程号，注册选课
        """

        # 获取学生信息
        studentID = self.ui.ID_input_5.text()
        courseID = self.ui.courseID_input_2.text()

        # 如果有空值，弹出警告
        if studentID == "":
            self.ui.ID_input_5.setFocus()
            self.ui.ID_input_5.setStyleSheet("border: 1px solid red;")
            self.ui.lineEdit_2.setText("不能为空")
            self.ui.lineEdit_2.setStyleSheet("color: red;")
            return
        else:
            self.ui.ID_input_5.setStyleSheet("")
        if courseID == "":
            self.ui.courseID_input_2.setFocus()
            self.ui.courseID_input_2.setStyleSheet("border: 1px solid red;")
            self.ui.lineEdit_2.setText("不能为空")
            self.ui.lineEdit_2.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseID_input_2.setStyleSheet("")

        # 判断学生是否存在
        if not self.studentManager.query(studentID):
            # 更改提示
            self.ui.lineEdit_2.setText("学号有误")
            self.ui.lineEdit_2.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseID_input_2.setStyleSheet("")
        # 判断课程是否存在
        if not self.courseManager.query(courseID):
            # 更改提示
            self.ui.lineEdit_2.setText("课号有误")
            self.ui.lineEdit_2.setStyleSheet("color: red;")
            return
        else:
            self.ui.courseID_input_2.setStyleSheet("")

        # 注册选课
        self.scManager.add(studentID, courseID)
        self.update()
        # 更改提示
        self.ui.lineEdit_2.setText("注册成功")
        self.ui.lineEdit_2.setStyleSheet("color: green;")

    def querySC(self):
        """
        输入学号，查询选课
        """

        # 获取学生信息
        studentID = self.ui.ID_input_6.text()

        # 判断学生是否存在
        if not self.studentManager.query(studentID):
            # 更改提示
            self.ui.textBrowser_3.setText("----学生信息不存在----\n")
            self.ui.textBrowser_3.setStyleSheet("color: red;")
            return

        # 查询选课
        mes = self.scManager.query(studentID)

        if studentID == "":
            # 查询全部
            if not mes:
                # 更改提示
                self.ui.textBrowser_3.setText("------无选课信息------\n")
                self.ui.textBrowser_3.setStyleSheet("color: red;")
            else:
                # 学号预留10位，课程号预留3位
                # 更改提示，组装信息
                output = "------选课信息------\n"
                for m in mes:
                    stuID = m['studentID']
                    couID = m['courseID']
                    s = "   " + stuID + " " * (11 - len(stuID)) + \
                        couID + " " * (3 - len(couID)) + "\n"
                    output += s
                self.ui.textBrowser_3.setText(output)
                self.ui.textBrowser_3.setStyleSheet("color: black;")
        else:
            # 查询单个
            if mes is None:
                # 更改提示
                self.ui.textBrowser_3.setText("----选课信息不存在----\n")
                self.ui.textBrowser_3.setStyleSheet("color: red;")
            else:
                # 学号预留10位，课程号预留3位
                # 更改提示，组装信息
                output = "------选课信息------\n"
                for m in mes:
                    stuID = m['studentID']
                    couID = m['courseID']
                    s = "   " + stuID + " " * (11 - len(stuID)) + \
                        couID + " " * (3 - len(couID)) + "\n"
                    output += s
                self.ui.textBrowser_3.setText(output)
                self.ui.textBrowser_3.setStyleSheet("color: black;")

    def removeSC(self):
        """
        获取学号，课程号，删除选课
        """
        # 获取下拉框信息
        studentID = self.ui.deleteStudentChoiceID.currentText()
        courseID = self.ui.deleteStudentChoiceCourseID.currentText()

        # 删除选课
        self.scManager.remove(studentID, courseID)
        self.update()

        # 更改提示
        self.ui.deleteChoiceState.setText("删除成功")
        self.ui.deleteChoiceState.setStyleSheet("color: green;")

    def update(self):
        """
        更新学生学号和课号
        """
        mes = []
        # 获取所有学生信息
        students = self.studentManager.query('')
        for stu in students:
            # 获取学生的所有课程
            courses = self.scManager.query(stu['studentID'])
            courseID = []
            for cou in courses:
                courseID.append(cou['courseID'])
            # 更新学生的课程信息
            mes.append({
                'studentID': stu['studentID'],
                'courseID': courseID
            })
        # 更新学生信息
        self.scList = mes

        # 更新下拉栏信息
        self.ui.deleteStudentChoiceID.clear()
        for i in range(len(self.scList)):
            self.ui.deleteStudentChoiceID.addItem(self.scList[i]['studentID'])

    def updateCourseID(self):
        """
        更新课程号
        """
        # 获取下拉栏选中的学生学号
        studentID = self.ui.deleteStudentChoiceID.currentText()

        # 更新下拉栏信息
        self.ui.deleteStudentChoiceCourseID.clear()
        for i in range(len(self.scList)):
            if self.scList[i]['studentID'] == studentID:
                for j in range(len(self.scList[i]['courseID'])):
                    self.ui.deleteStudentChoiceCourseID.addItem(self.scList[i]['courseID'][j])


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    # 创建主窗口
    main = Main()
    # 显示窗口
    main.show()

    sys.exit(app.exec_())
