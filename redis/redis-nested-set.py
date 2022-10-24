import redis

redis_client = redis.Redis(host='localhost', port='6379')

# To save a nested object in Redis.
# For storing nested objects, we can make use of the “hset” function but it allows only one level of nesting

redis_client.hset('fest-set', 'name', 'hacktoberfest-set')
value = redis_client.hget('fest-set', 'name')
print(value)
