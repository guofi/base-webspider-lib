import pymongo
from pymongo import MongoClient

'''
delete_one() 和 delete_many()
'''


def fun():
    client = MongoClient('mongodb://root:123456@1.2.3.4:27017')
    db = client['test']
    collection = db['students']

    result = collection.delete_many({'name': 'Jordan'})
    print(result)


'''
DeleteResult({'n': 1, 'ok': 1.0}, acknowledged=True)


'''
if __name__ == "__main__":
    fun()
