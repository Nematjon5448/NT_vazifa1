import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True, db=0)

def blpop(key, time: int):
    result = redis_client.blpop(key, time)
    return result

def brpop(key, time: int):
    result = redis_client.brpop(key, time)
    return result

def brpoplpush(key1, key2, time):
    result = redis_client.brpoplpush(key1, key2, time)
    return result

def lindex(key, index: int):
    result = redis_client.lindex(key, index)
    return result

def linsert(key, before_or_after: str, refvalue: str, value: str) -> int:
    result = redis_client.linsert(key, before_or_after, refvalue, value)
    return result

def llen(key) -> int:
    result = redis_client.llen(key)
    return result

def lpop(key):
    result = redis_client.lpop(key)
    return result

def lpush(key, *values) -> int:
    result = redis_client.lpush(key, *values)
    return result

def lpushx(key, *values) -> int:
    result = redis_client.lpushx(key, *values)
    return result

def lrange(key, start: int, end: int) -> list:
    result = redis_client.lrange(key, start, end)
    return result

def lrem(key, count: int, value: str) -> int:
    result = redis_client.lrem(key, count, value)
    return result

def lset(key, index: int, value: str):
    result = redis_client.lset(key, index, value)
    return result

def rpop(key):
    result = redis_client.rpop(key)
    return result

def rpoplpush(key1, key2):
    result = redis_client.rpoplpush(key1, key2)
    return result

def rpush(key, *values: str) -> int:
    result = redis_client.rpush(key, *values)
    return result

def rpushx(key, *values: str) -> int:
    result = redis_client.rpushx(key, *values)
    return result

if __name__ == '__main__':
    # print(blpop('users', 20))
    # print(brpop('users', 20))
    # print(brpoplpush('users', 'new_users', 20))
    # print(lindex('new_users', 2))
    # print(linsert('new_users', 'BEFORE', 'Nematjon', 'Azizbek'))
    # print(type(llen('new_users')))
    # print(lpop('new_users'))
    # print(lpush('users', 'Ziyodullo', 'Abdullo', 'Bobur'))
    # print(lpushx('users', 'Xadiyatullo'))
    # print(lrange('users', 0, -1))
    # print(lrem('users', 2, 'Bobur'))
    # print(lset('users', 2, 'Nematjon'))
    # print(rpop('users'))
    # print(rpoplpush('users', 'new_users'))
    # print(rpush('users', 'Saidamirxon', 'Humoyun'))
    # print(rpushx('users', 'Ikrom'))