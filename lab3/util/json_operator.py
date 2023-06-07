# Encoding: utf-8
"""
json文件读写操作
"""
import json
import os


def read_json(path):
    """
    读取json文件
    :return: json对象
    """
    if not path.endswith('.json'):
        path += '.json'
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        data = json.load(f)
    return data


def write_json(path, ProData):
    """
    写入json文件
    :param path: 文件路径
    :param ProData: 数据
    :return:
    """
    if not path.endswith('.json'):
        path += '.json'
    with open(path, 'w') as f:
        json.dump(ProData, f)