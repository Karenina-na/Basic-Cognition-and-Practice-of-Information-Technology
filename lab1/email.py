import re

if __name__ == "__main__":
    email = input("请输入邮箱:")
    # 判断邮箱是否合法
    if re.match(r"^\w+@\w+\.\w+$", email):
        print("邮箱合法")
    else:
        print("邮箱不合法")