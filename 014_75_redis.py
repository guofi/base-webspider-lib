from redis import StrictRedis

'''
redis 读写
'''


def fun():
    redis = StrictRedis(host='1.2.3.4', port=6379, db=0, password='')
    redis.set('name', 'Lily')
    print(redis.get('name'))


'''

b'Lily'
'''
if __name__ == "__main__":
    fun()
