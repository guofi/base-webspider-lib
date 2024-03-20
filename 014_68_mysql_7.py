import pymysql

'''
 spider.students
查询  while  fetchone

这样每循环一次，指针就会偏移一条数据，随用随取，简单高效
'''


def fun():
    sql = 'SELECT * FROM students WHERE age >= 20'
    db = pymysql.connect(host='1.2.3.4', user='root', password='123456', port=3306, db='spider')
    cursor = db.cursor()

    cursor.execute('set names utf8')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('Row: ', row)
            row = cursor.fetchone()

    except Exception as ex:
        print("Failed")
        print('异常: %s' % ex)

        db.rollback()
        db.close()


if __name__ == '__main__':
    fun()
