# 获取项目的绝对路径方法
import logging
import shutil
from logging import handlers
import os


# ====================
# 获取项目的绝对路径
def get_file_path():
    dirname = os.path.dirname(__file__)
    return dirname


if __name__ == '__main__':
    path = get_file_path()
    print(path)


# 设置一个配置类,目前只用来设置日志器
class MyConfig:
    # 1 定义一个初始化日志配置的函数：初始化日志的输出路径（例如：输出到控制和日志文件中）
    @classmethod
    # 注释了控制台处理器, 就不显示在控制台了
    def init_logging(cls, logger_name):
        # 2 创建日志器
        logger = logging.getLogger()
        # 3 设置日志等级:Debug,Info,Warn,Error,critical
        logger.setLevel(logging.INFO)
        # 4 创建处理器，通过处理控制日志的打印（打印到控制台和日志文件中）
        # 创建控制台处理器
        # sh = logging.StreamHandler()
        # 创建文件处理器：文件处理的作用是把日志写道日志文件当中，如果我们不管理日志文件，那么日志文件会越来越大
        # 这种情况下，我们需要拆分日志，按大小拆分和按时间拆分（掌握按时间拆分），使用logging模块中的拆分日志的工具来进行
        # when='D', interval=1 代表两次运行的间隔时间超过 1天就会拆分日志 , 一天一个日志文件,超过三个文件就开始覆盖一个文件
        # backupCount:保留的日志文件数量
        fh = logging.handlers.TimedRotatingFileHandler(get_file_path() + "/Log/%s.log" % logger_name,
                                                       when='D', interval=1, backupCount=3, encoding='utf-8')
        # 5 设置日志的格式，所以需要创建格式和格式化器
        fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
        formatter = logging.Formatter(fmt)
        # 6 将格式化器添加到处理器当中
        # 输出到控制台的处理器
        # sh.setFormatter(formatter)
        #  输出到文件的处理器
        fh.setFormatter(formatter)
        # 7 将处理器添加到日志器当中,
        # logger.addHandler(sh)
        logger.addHandler(fh)
        return logger

    @classmethod
    def init_folder(cls):
        # 先判断文件夹是否存在，如果存在，先删除文件夹，避免太多无用文件占用内存
        if os.path.exists(get_file_path() + "/Download/"):
            shutil.rmtree(get_file_path() + "/Download/")
        if os.path.exists(get_file_path() + "/Save/"):
            shutil.rmtree(get_file_path() + "/Save/")
        # 重新创建文件夹
        os.makedirs(get_file_path() + "/Download/")
        os.makedirs(get_file_path() + "/Save/")
