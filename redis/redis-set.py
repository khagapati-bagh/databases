import redis

redis_client = redis.Redis(host='localhost', port='6379')

# To set a key-value pair where the value is of a set data type, we use the “sadd” function.
languages = ["c", "c++", "java", "python", "c++"]
redis_client.sadd('languages', *languages)

# To get all the values of languages that we just stored, we can use the “smembers” function.
value = redis_client.smembers('languages')
print(value)
