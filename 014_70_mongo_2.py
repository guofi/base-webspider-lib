import pymongo
from pymongo import MongoClient

'''

插入多条
insert_many


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

    student2 = {
        'id': '20170102',
        'name': 'Mike',
        'age': 21,
        'gender': 'female'
    }

    result = collection.insert_many([student, student2])
    print(result)


'''
InsertManyResult([ObjectId('65faa9973738ae2cb55424c4'), ObjectId('65faa9973738ae2cb55424c5')], acknowledged=True)

'''
if __name__ == "__main__":
    fun()
