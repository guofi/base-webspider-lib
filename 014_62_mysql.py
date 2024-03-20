import pymysql

'''
创建数据库 spider
'''
def fun():
    db = pymysql.connect(host='1.2.3.4', user='root', password='123456', port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    '''
    mysql version: ('5.7.43',)
    '''
    # print('mysql version:', data)
    cursor.execute("CREATE DATABASE IF NOT EXISTS spider DEFAULT CHARACTER SET utf8mb4")
    db.close()


if __name__ == '__main__':
    fun()
