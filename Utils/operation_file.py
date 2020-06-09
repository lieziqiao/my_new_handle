# 封装操作文件的类
import my_config
import yaml
import json
from collections import OrderedDict
# 封装一个类, 用来管理对文件的操作, 暂时只有对yaml 和 json 文件的操作


class FileTools:
    # 对yaml 文件进行操作
    @classmethod
    # 传递的文件,只需要写项目目录下的路径即可
    def operation_file_yaml(cls, file_path, method='r', key_index=None,  write_data=None):
        # 获取 项目的根目录
        global_path = my_config.get_file_path()
        filename = global_path + file_path

        # 如果是读取yaml文件, 而且yaml文件的格式必须是三层嵌套的字典,
        if (method == "r") and (key_index is not None):
            with open(filename, method, encoding='utf8') as f:
                # 根据键名提取对应的数据
                data = yaml.load(f, Loader=yaml.FullLoader)[key_index]
                # 转换成列表套字典
                data = list(data.values())
            return data
        else:
            # 将数据写入yaml文件中
            with open(filename, method, encoding='utf') as f:
                yaml.dump(write_data, f)

    # 获取JSON数据并返回元祖类型的数据
    @classmethod
    def get_json_case_data(cls, filename):
        with open(filename, encoding="utf-8") as f:
            case_data = json.load(f, object_pairs_hook=OrderedDict)
        case_list = []
        # 获取Json的数据方法, json数据从文件里读取过来就是字典, 要在测试中使用的是它的键对应的键值
        for case in case_data.values():
            case_list.append(tuple(case.values()))
        return case_list





