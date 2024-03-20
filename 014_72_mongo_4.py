import pymongo
from pymongo import MongoClient

'''

更新
$操作符，可以用$set、$inc、$push进行更新操作，网上有人测试过使用$set和$inc时间区别不大，但是$push时间慢于前两者

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

    condition = {'name': 'Mike'}
    student = collection.find_one(condition)
    # student['age'] = 24
    # result = collection.update_one(condition, {"$set": {'age': '18'}})
    result = collection.update_one(condition, {"$set": {'age': '18'}})
    print(result)


'''
UpdateResult({'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}, acknowledged=True)
'''
if __name__ == "__main__":
    fun()
