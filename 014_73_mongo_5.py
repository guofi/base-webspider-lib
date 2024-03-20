import pymongo
from pymongo import MongoClient

'''

更新
$操作符，可以用$set、$inc、$push进行更新操作，网上有人测试过使用$set和$inc时间区别不大，但是$push时间慢于前两者

update_many() 方法，则会将所有符合条件的数据都更新
'''


def fun():
    client = MongoClient('mongodb://root:123456@1.2.3.4:27017')

    db = client['test']
    collection = db['students']
    # student = {
    #     'id': '20170101',
    #     'name': 'Jordan',
    #     'age': 20,
    #     'gender': 'male'
    # }
    #
    # student2 = {
    #     'id': '20170102',
    #     'name': 'Mike',
    #     'age': 21,
    #     'gender': 'female'
    # }

    condition = {'age': {'$gt': 10}}

    # result = collection.update_one(condition, {'$inc': {'age': 1}})
    result = collection.update_many(condition, {'$inc': {'age': 1}})
    print(result)


'''
UpdateResult({'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)

UpdateResult({'n': 2, 'nModified': 2, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)
'''
if __name__ == "__main__":
    fun()
