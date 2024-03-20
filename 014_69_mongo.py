import pymongo
from pymongo import MongoClient

'''

插入一条

在 MongoDB 中，每条数据其实都有一个_id 属性来唯一标识。如果没有显式指明该属性，MongoDB 会自动产生一个 ObjectId 类型的_id 属性。
insert_one() 方法会在执行后返回_id 值。

'''


def fun():
    # client = pymongo.MongoClient(host='1.2.3.4', port=27017)
    client = MongoClient('mongodb://root:123456@1.2.3.4:27017')

    # db = client.test
    db = client['test']
    # collection = db.students
    collection = db['students']
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
    result = collection.insert_one(student)
    print(result)


'''
InsertOneResult(ObjectId('65faa85100c0a611c72823e9'), acknowledged=True)
'''
if __name__ == "__main__":
    fun()
