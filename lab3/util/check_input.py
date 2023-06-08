def checkName(name):
    """
    检查用户名是否合法
    """
    if len(name) > 3:
        return False
    return True


def checkStudentID(ID):
    """
    检查学号是否合法
    """
    if len(ID) > 10:
        return False
    return True


def checkAge(age):
    """
    检查年龄是否合法
    """
    if len(age) > 2:
        return False
    return True


def checkClass(cls):
    """
    检查班级是否合法
    """
    if len(cls) > 1:
        return False
    return True


def checkCourseID(CID):
    """
    检查课程号是否合法
    """
    if len(CID) > 3:
        return False
    return True


def checkCourseName(CName):
    """
    检查课程名是否合法
    """
    if len(CName) > 4:
        return False
    return True


def checkCourseCredit(credit):
    """
    检查学分是否合法
    """
    if len(credit) > 1:
        return False
    return True


def checkTeacherName(TName):
    """
    检查教师名是否合法
    """
    if len(TName) > 3:
        return False
    return True
