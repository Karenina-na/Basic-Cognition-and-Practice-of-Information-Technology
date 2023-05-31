if __name__ == '__main__':
    uname = input("请输入姓名:")
    passwd = input("请输入性别:")
    email = input("请输入地址:")
    tel = input("请输入生日:")
    address = input("请输入电话:")
    age = input("请输入邮箱:")
    print("====================您的注册信息==================== %格式")
    print("姓名:%s \n 性别:%s \n 地址:%s \n 生日:%s \n 电话:%s \n 邮箱:%s" % (uname, passwd, email, tel, address, age))

    print("====================您的注册信息==================== {}格式")
    print("姓名:{} \n 性别:{} \n 地址:{} \n 生日:{} \n 电话:{} \n 邮箱:{}".format(uname, passwd, email, tel, address, age))