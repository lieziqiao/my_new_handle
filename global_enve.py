from my_config import MyConfig
import my_config
# 设置全局变量, 解决有时候相互引用出错的问题,用这个文件存储全局变量
# 实例化日志器对象
my_logger = MyConfig.init_logging("my_logger")

# 程序启动时初始化保存不重要数据的文件夹
MyConfig.init_folder()

# 项目地址, alfred2.3登陆url
project_url = "https://www.baidu.com/"
# 常用的超管账号
username = ""
password = ""

# 这个号是我本地调试使用的
# username = "docking"
# password = "123456"


# 导出文件保存路径
report_address = str(my_config.get_file_path())+"\\Download"
# 添加地点中的地点名字
location_name = list()

# 添加地点组的地点组名字
group_name = None


# UI版本的版本名字
ui_version_name = None

#  统计滑屏次数
repeat = 0

