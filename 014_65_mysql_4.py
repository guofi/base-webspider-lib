import pymysql

'''
 spider.students
 插入数据
 % s 格式化符

这里首先定义了长度为 1 的数组 ['% s']，然后用乘法将其扩充为 ['% s', '% s', '% s']，再调用 join 方法，
最终变成 % s, % s, % s。最后，我们再利用字符串的 format 方法将表名、字段名和占位符构造出来。最终的 SQL 语句就被动态构造成了
 
'''


def fun():
    data = {
        'id': '10000',
        'name': 'Bob2',
        'age': 22
    }

    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['% s'] * len(data))

    print(tuple(data.values()))

    sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

    print(sql)

    db = pymysql.connect(host='1.2.3.4', user='root', password='123456', port=3306, db='spider')
    cursor = db.cursor()

    cursor.execute('set names utf8')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

    # sql = 'INSERT INTO spider.students(id, name, age) values(% s, % s, % s)'

    try:
        cursor.execute(sql, tuple(data.values()))
        print("Success")
        db.commit()
    except Exception as ex:
        print("Failed")
        print('异常: %s' % ex)

        db.rollback()
        db.close()


if __name__ == '__main__':
    fun()
