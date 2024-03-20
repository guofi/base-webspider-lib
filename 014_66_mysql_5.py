import pymysql

'''
 spider.students
插入数据(存在则更新，不存在则插入)
 这里就变成了 6 个 % s。所以在后面的 execute 方法的第二个参数元组就需要乘以 2 变成原来的 2 倍
'''


def fun():
    data = {
        'id': '10000',
        'name': 'Bob2',
        'age': 23
    }

    table = 'students'
    keys = ', '.join(data.keys())
    values = ', '.join(['% s'] * len(data))

    print(tuple(data.values()))

    sql = 'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,
                                                                                           values=values)
    update = ','.join(["{key} = % s".format(key=key) for key in data])

    '''
    INSERT INTO students (id, name, age) VALUES (% s, % s, % s) ON DUPLICATE KEY UPDATE id = % s,name = % s,age = % s
    '''
    sql += update
    # print(sql)

    db = pymysql.connect(host='1.2.3.4', user='root', password='123456', port=3306, db='spider')
    cursor = db.cursor()

    cursor.execute('set names utf8')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')

    try:
        cursor.execute(sql, tuple(data.values()) * 2)
        print("Success")
        db.commit()
    except Exception as ex:
        print("Failed")
        print('异常: %s' % ex)

        db.rollback()
        db.close()


if __name__ == '__main__':
    fun()
