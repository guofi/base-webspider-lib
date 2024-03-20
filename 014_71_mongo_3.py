import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

'''

查询

find_one()

find():

回结果是 Cursor 类型，它相当于一个生成器，我们需要遍历取到所有的结果，其中每个结果都是字典类型。
'''


def fun():
    # client = pymongo.MongoClient(host='1.2.3.4', port=27017)
    client = MongoClient('mongodb://root:123456@1.2.3.4:27017')
    db = client['test']
    collection = db['students']
    result = collection.find_one({'_id': ObjectId('65faa9973738ae2cb55424c5')})
    # print(result)
    result2 = collection.find({'age': 20})
    '''
    <pymongo.cursor.Cursor object at 0x00000233F0A5B9A0>
    '''
    # print(result2)
    result3 = collection.find({'age': {'$gt': 20}})

    '''
    {'_id': ObjectId('65faa9973738ae2cb55424c5'), 'id': '20170102', 'name': 'Mike', 'age': 21, 'gender': 'female'}
    '''
    # for res in result3:
    #     print(res)

    '''
    正则匹配
    {'_id': ObjectId('65faa9973738ae2cb55424c5'), 'id': '20170102', 'name': 'Mike', 'age': 21, 'gender': 'female'}
    '''
    result4 = collection.find({'name': {'$regex': '^M.*'}})
    # for res in result4:
    #     print(res)
    '''
    排序
    ['Jordan', 'Jordan', 'Mike']
    '''
    result5 = collection.find().sort('name', pymongo.ASCENDING)

    '''
    在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，因为这样很可能导致内存溢出
    ['Jordan', 'Mike']
    '''
    result6 = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(2)
    # print([result['name'] for result in result6])

    '''
    ['Jordan', 'Jordan']
    '''
    result7 = collection.find({'_id': {'$lt': ObjectId('65faa9973738ae2cb55424c5')}})
    print([result['name'] for result in result7])


'''
{'_id': ObjectId('65faa85100c0a611c72823e9'), 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
{'_id': ObjectId('65faa9973738ae2cb55424c4'), 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
'''
if __name__ == "__main__":
    fun()
