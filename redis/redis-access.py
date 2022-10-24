import redis

redis = redis.Redis(host='localhost', port='6379')

# Simple key value pair
redis.set('mypykey', 'Hello from Python!')
value = redis.get('mypykey')
print(value)

# Multiple-key value pairs
data = {
    'fest': 'hacktoberfest',
    'year': '2022'
}
redis.mset(data)
value = redis.get('fest')
print(value)
