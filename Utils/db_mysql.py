import pymysql


# 操作数据的类
class DBUtils:
    # 初始化, 设置默认连接的数据库
    def __init__(self, host="", user="", password="", database=""):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 这个 enter方法 会使用 with 语法的时候, 进入函数时会先执行 enter的代码
    def __enter__(self):
        # 与数据库建立连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                    database=self.database)

        # 获取游标
        self.cursor = self.conn.cursor()
        return self.cursor

    # 退出with 语句块的时候, 会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 查询并不需要提交事务, 但是新增, 修改和删除需要提交事务,否则数据并没有真正修改成功
        # 本方法只支持单次修改数据库的数据, 如果是一个复杂的事务的话,另外单独写,不要使用这里,以免对数据造成污染
        self.conn.commit()
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
