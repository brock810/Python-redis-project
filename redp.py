import redis
r = redis.Redis(host='localhost', port=6379, db=0)

r.set('hello_there', 'General kenobi')

value = r.get('hello_there')
if value: 
    print(value.decode('utf-8'))

r.incr('mycounter')
counter_value = r.get('mycounter')
print("Counter:", counter_value.decode('utf-8'))

if r.exists('hello_there'):
    print("Key 'hello_there' exists")


if not r.exists ('hello_there'):
    print("Key 'hello_there' does not exist")
