
if __name__ == "__main__":
    email = input("请输入邮箱:")
    if email.find("@") != -1 and email.find(".") != -1:
        print("邮箱格式正确")
    else:
        print("邮箱格式错误")