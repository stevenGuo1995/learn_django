import pymysql

DB_HOST = '192.168.14.10'
DB_USER = 'root'
DB_PASSWORD = '1234.Com'
DB_NAME = 'book'

if __name__ == '__main__':
    username = 'xiewd'
    password = 'guoxf666'
    # 连接数据库
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    # 创建一个操作数据库的指针
    cursor = conn.cursor()

    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    if password in res:
        print('yes')
    else:
        print('用户名或密码错误！')