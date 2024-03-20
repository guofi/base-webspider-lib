import pymysql

'''
 spider.students
 插入数据
 % s 格式化符
 值统一用元组传递
 
'''


def fun():
    id = '200000'
    user = 'Bob'
    age = 20

    db = pymysql.connect(host='1.2.3.4', user='root', password='123456', port=3306)
    cursor = db.cursor()

    sql = 'INSERT INTO spider.students(id, name, age) values(% s, % s, % s)'

    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ == '__main__':
    fun()
