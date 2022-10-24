import redis

redis = redis.Redis(host= 'localhost', port= '6379')
redis.set('mypykey', 'Hello from Python!')
value = redis.get('mypykey')
print(value)
