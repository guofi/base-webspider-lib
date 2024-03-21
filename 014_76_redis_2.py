from redis import StrictRedis, ConnectionPool

'''
redis 读写
    ConnectionPool 
ConnectionPool 还支持通过 URL 来构建。URL 的格式支持有如下 3 种
    
Redis TCP 连接、Redis TCP+SSL 连接、Redis UNIX socket 连接
    
redis://[:password]@host:port/db  
rediss://[:password]@host:port/db  
unix://[:password]@/path/to/socket.sock?db=db
'''


def fun():
    pool = ConnectionPool(host='1.2.3.4', port=6379, db=0, password='')
    # redis = StrictRedis(host='1.2.3.4', port=6379, db=0, password='')
    redis = StrictRedis(connection_pool=pool)
    redis.set('name-2', 'Lily-2')
    print(redis.get('name-2'))


'''

b'Lily-2'
'''
if __name__ == "__main__":
    fun()
