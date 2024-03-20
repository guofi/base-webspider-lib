import pymysql

'''
创建表 spider.students
'''


def fun():
    db = pymysql.connect(host='1.2.3.4', user='root', password='123456', port=3306)
    cursor = db.cursor()

    sql = ('CREATE TABLE IF NOT EXISTS spider.students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, '
           'age INT NOT NULL, PRIMARY KEY (id))')
    cursor.execute(sql)
    db.close()


if __name__ == '__main__':
    fun()
